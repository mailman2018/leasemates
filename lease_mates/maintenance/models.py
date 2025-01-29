from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class MaintenanceRequest(models.Model):
    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    tenant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='maintenance_requests')
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    landlord_notified = models.BooleanField(default=False)
    suggested_fix = models.TextField(blank=True, null=True)
    third_party_suggestions = models.TextField(blank=True, null=True)
    tenant_feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Request #{self.id} - {self.status}"
