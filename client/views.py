from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from client.models import Client
from client.serializers import ClientSerializer


@permission_classes([IsAuthenticated])
class ClientSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('last_name', 'email')

    def get_queryset(self):
        if self.request.user.team == 'MNG':
            return Client.objects.all()
        else:
            return Client.objects.filter(sale_contact=self.request.user)
