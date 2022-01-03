from rest_framework import viewsets

from event.models import Event
from event.serializers import EventSerializer


class EventSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        if self.request.user.team == 'VDR':
            return Event.objects.filter(contract__sale_contact=self.request.user)
        elif self.request.user.team == 'MNG':
            return Event.objects.all()
        else:
            return Event.objects.filter(support_contact=self.request.user)
