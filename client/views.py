from rest_framework import viewsets

from client.models import Client
from client.serializers import ClientSerializer


class ClientSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
