from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from .serializers import EventSerializer

class event_det(APIView):
    def get(self, request, Event_ID, date_of_event):
        try:
            event = Event.objects.get(Event_ID=Event_ID, doe=date_of_event)
            serializer = EventSerializer(event)
            return Response(serializer.data)
        except Event.DoesNotExist:
            return Response({"message": "Event not found"}, status=status.HTTP_404_NOT_FOUND)
        












        