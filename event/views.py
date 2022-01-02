from rest_framework import viewsets

from event.models import Event
from event.serializers import EventSerializer


class EventSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
