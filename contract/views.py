from rest_framework import viewsets

from contract.models import Contract
from contract.serializers import ContractSerializer


class ContractSet(viewsets.ModelViewSet):
    serializer_class = ContractSerializer

    def get_queryset(self):
        if self.request.user.team == 'MNG':
            return Contract.objects.all()
        else:
            return Contract.objects.filter(sale_contact=self.request.user)
