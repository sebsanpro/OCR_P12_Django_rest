from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from event.models import Event
from event.serializers import EventSerializer


@permission_classes([IsAuthenticated])
class EventSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('client__last_name', 'client__email', 'event_date')

    def get_queryset(self):
        if self.request.user.team == 'VDR':
            return Event.objects.filter(contract__sale_contact=self.request.user)
        elif self.request.user.team == 'MNG':
            return Event.objects.all()
        else:
            return Event.objects.filter(support_contact=self.request.user)
