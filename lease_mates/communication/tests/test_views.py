from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from communication.models import Message, Announcement

class MessageAPITestCase(APITestCase):
    def setUp(self):
        # Create two test users
        self.sender = User.objects.create_user(username='sender', password='test123')
        self.recipient = User.objects.create_user(username='recipient', password='test123')
        self.client.force_authenticate(user=self.sender)

        # Create a test message
        self.message = Message.objects.create(
            subject="Test Subject",
            body="Test Body",
            sender=self.sender,
            recipient=self.recipient
        )

    def test_create_message(self):
        data = {
            "subject": "Hello",
            "body": "This is a test message",
            "sender": self.sender.id,
            "recipient": self.recipient.id
        }
        response = self.client.post('/api/messages/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['subject'], "Hello")

    def test_get_message(self):
        response = self.client.get(f'/api/messages/{self.message.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['subject'], self.message.subject)

    def test_update_message(self):
        data = {
            "subject": "Updated Subject",
            "body": "Updated Body",
            "sender": self.sender.id,
            "recipient": self.recipient.id
        }
        response = self.client.put(f'/api/messages/{self.message.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['subject'], "Updated Subject")

    def test_delete_message(self):
        response = self.client.delete(f'/api/messages/{self.message.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class AnnouncementAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.landlord = User.objects.create_user(username='landlord', password='test123')
        self.client.force_authenticate(user=self.landlord)

        # Create a test announcement
        self.announcement = Announcement.objects.create(
            title="Test Announcement",
            content="This is a test announcement",
            landlord=self.landlord
        )

    def test_create_announcement(self):
        data = {
            "title": "New Announcement",
            "content": "This is a new announcement",
            "landlord": self.landlord.id
        }
        response = self.client.post('/api/announcements/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "New Announcement")

    def test_get_announcement(self):
        response = self.client.get(f'/api/announcements/{self.announcement.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.announcement.title)

    def test_update_announcement(self):
        data = {
            "title": "Updated Announcement",
            "content": "Updated content",
            "landlord": self.landlord.id
        }
        response = self.client.put(f'/api/announcements/{self.announcement.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Announcement")

    def test_delete_announcement(self):
        response = self.client.delete(f'/api/announcements/{self.announcement.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
