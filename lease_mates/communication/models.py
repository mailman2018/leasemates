from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Message(models.Model):
    MESSAGE_TYPES = [
        ('general', 'General'),
        ('maintenance', 'Maintenance'),
        ('payment', 'Payment'),
        ('emergency', 'Emergency'),
        ('lease', 'Lease'),
    ]

    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    message_type = models.CharField(max_length=20, choices=MESSAGE_TYPES, default='general')
    subject = models.CharField(max_length=255)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    is_urgent = models.BooleanField(default=False)
    related_maintenance = models.ForeignKey('maintenance.MaintenanceRequest', on_delete=models.SET_NULL, null=True, blank=True)
    related_payment = models.ForeignKey('properties.Payment', on_delete=models.SET_NULL, null=True, blank=True)
    related_lease = models.ForeignKey('properties.Lease', on_delete=models.SET_NULL, null=True, blank=True)
    attachments = models.ManyToManyField('MessageAttachment', blank=True)
    read_at = models.DateTimeField(null=True, blank=True)
    reply_to = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='replies')

    def __str__(self):
        return f"Message from {self.sender} to {self.recipient}"

    def mark_as_read(self):
        self.is_read = True
        self.read_at = timezone.now()
        self.save()

class MessageAttachment(models.Model):
    file = models.FileField(upload_to='message_attachments/')
    filename = models.CharField(max_length=255)
    file_type = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.filename

class Announcement(models.Model):
    ANNOUNCEMENT_TYPES = [
        ('general', 'General'),
        ('maintenance', 'Maintenance'),
        ('emergency', 'Emergency'),
        ('payment', 'Payment'),
        ('event', 'Event'),
    ]

    landlord = models.ForeignKey(User, related_name='announcements', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    announcement_type = models.CharField(max_length=20, choices=ANNOUNCEMENT_TYPES, default='general')
    timestamp = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_urgent = models.BooleanField(default=False)
    target_units = models.ManyToManyField('properties.Unit', blank=True)
    attachments = models.ManyToManyField('AnnouncementAttachment', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def is_expired(self):
        if self.expires_at:
            return timezone.now() > self.expires_at
        return False

class AnnouncementAttachment(models.Model):
    file = models.FileField(upload_to='announcement_attachments/')
    filename = models.CharField(max_length=255)
    file_type = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.filename

class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('message', 'New Message'),
        ('maintenance', 'Maintenance Update'),
        ('payment', 'Payment Reminder'),
        ('announcement', 'New Announcement'),
        ('lease', 'Lease Update'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    title = models.CharField(max_length=255)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True, blank=True)
    related_object_id = models.IntegerField(null=True, blank=True)
    related_object_type = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.notification_type} notification for {self.user}"

    def mark_as_read(self):
        self.is_read = True
        self.read_at = timezone.now()
        self.save()
