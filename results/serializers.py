from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['Event_ID', 'Title', 'Attendee_No', 'doe', 'Location', 'Organizer','Event_Category']


















