from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class MaintenanceRequest(models.Model):
    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('assigned', 'Assigned'),
        ('in_progress', 'In Progress'),
        ('pending_parts', 'Pending Parts'),
        ('pending_approval', 'Pending Approval'),
        ('resolved', 'Resolved'),
        ('cancelled', 'Cancelled'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]

    CATEGORY_CHOICES = [
        ('plumbing', 'Plumbing'),
        ('electrical', 'Electrical'),
        ('appliance', 'Appliance'),
        ('heating', 'Heating/Cooling'),
        ('structural', 'Structural'),
        ('pest_control', 'Pest Control'),
        ('other', 'Other'),
    ]

    tenant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='maintenance_requests')
    unit = models.ForeignKey('properties.Unit', on_delete=models.CASCADE, related_name='maintenance_requests')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    estimated_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    actual_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_maintenance')
    landlord_notified = models.BooleanField(default=False)
    suggested_fix = models.TextField(blank=True, null=True)
    third_party_suggestions = models.TextField(blank=True, null=True)
    tenant_feedback = models.TextField(blank=True, null=True)
    completion_date = models.DateTimeField(null=True, blank=True)
    photos = models.ManyToManyField('MaintenancePhoto', blank=True)
    is_emergency = models.BooleanField(default=False)
    preferred_contact_method = models.CharField(max_length=20, choices=[
        ('email', 'Email'),
        ('phone', 'Phone'),
        ('text', 'Text Message'),
    ], default='email')
    preferred_contact_time = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.status}"

    def mark_as_resolved(self):
        self.status = 'resolved'
        self.completion_date = timezone.now()
        self.save()

    def assign_to(self, user):
        self.assigned_to = user
        self.status = 'assigned'
        self.save()

    def update_status(self, new_status):
        self.status = new_status
        if new_status == 'resolved':
            self.completion_date = timezone.now()
        self.save()

class MaintenancePhoto(models.Model):
    image = models.ImageField(upload_to='maintenance_photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=True)
    is_before = models.BooleanField(default=True)  # True for before photos, False for after photos

    def __str__(self):
        return f"Photo {self.id} - {'Before' if self.is_before else 'After'}"

class MaintenanceSchedule(models.Model):
    unit = models.ForeignKey('properties.Unit', on_delete=models.CASCADE, related_name='maintenance_schedules')
    title = models.CharField(max_length=255)
    description = models.TextField()
    frequency = models.CharField(max_length=20, choices=[
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('yearly', 'Yearly'),
    ])
    last_performed = models.DateTimeField(null=True, blank=True)
    next_due = models.DateTimeField()
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.frequency}"

    def mark_as_completed(self):
        self.last_performed = timezone.now()
        self.save()
