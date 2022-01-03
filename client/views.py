from rest_framework import viewsets

from client.models import Client
from client.serializers import ClientSerializer


class ClientSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer

    def get_queryset(self):
        if self.request.user.team == 'MNG':
            return Client.objects.all()
        else:
            return Client.objects.filter(sale_contact=self.request.user)
