from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import MaintenanceRequest
from .serializers import MaintenanceRequestSerializer
from openai import OpenAI

client = OpenAI(api_key="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")  # For ChatGPT API integration

# ChatGPT Helper Function
def get_chatgpt_response(prompt):
      # Replace with your OpenAI key
    response = client.chat.completions.create(model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    max_tokens=200,
    temperature=0.7)
    return response.choices[0].message.content.strip()


class MaintenanceRequestViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceRequest.objects.all()
    serializer_class = MaintenanceRequestSerializer
    permission_classes = [IsAuthenticated]

    # Overriding create method to include AI-powered suggestions
    def create(self, request, *args, **kwargs):
        # Step 1: Validate the data (excluding 'tenant' from client input)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Step 2: Save the request and set the tenant as the logged-in user
        maintenance_request = serializer.save(tenant=request.user)  # Assign tenant automatically

        # Step 3: Generate AI suggestions for a fix
        prompt = f"Suggest a fix for the following issue reported by a tenant: {maintenance_request.description}"
        suggested_fix = get_chatgpt_response(prompt)

        # Step 4: Save AI suggestions in the model
        maintenance_request.suggested_fix = suggested_fix
        maintenance_request.save()

        # Step 5: Return the response with suggestions
        return Response({
            "message": "Maintenance request submitted!",
            "maintenance_request": MaintenanceRequestSerializer(maintenance_request).data,
            "suggested_fix": suggested_fix,
        }, status=status.HTTP_201_CREATED)

    # Handle updates, such as tenant dissatisfaction
    def update(self, request, *args, **kwargs):
        maintenance_request = self.get_object()
        if 'tenant_feedback' in request.data:
            if request.data['tenant_feedback'].lower() == 'unsatisfied':
                # Notify landlord
                maintenance_request.landlord_notified = True

                # Generate potential third-party contacts via ChatGPT
                prompt = f"List potential third-party services to resolve this issue: {maintenance_request.description}"
                third_party_suggestions = get_chatgpt_response(prompt)

                maintenance_request.third_party_suggestions = third_party_suggestions
                maintenance_request.save()

        return super().update(request, *args, **kwargs)
