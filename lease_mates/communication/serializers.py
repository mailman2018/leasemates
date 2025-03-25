from rest_framework import serializers
from .models import Message, Announcement


#serializes models so that they could be converted to json to be used in our api
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'
