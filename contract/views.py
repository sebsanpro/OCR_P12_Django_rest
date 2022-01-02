from rest_framework import viewsets

from contract.models import Contract
from contract.serializers import ContractSerializer


class ContractSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
