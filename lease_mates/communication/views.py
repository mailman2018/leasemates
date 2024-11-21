from rest_framework import viewsets
from .models import Message, Announcement
from .serializers import MessageSerializer, AnnouncementSerializer

# Simplify CRUD operations by combining List, Retrieve, Create, Update, and Delete views into a single class.

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
