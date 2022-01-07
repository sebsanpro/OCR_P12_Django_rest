from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from contract.models import Contract
from contract.serializers import ContractSerializer


@permission_classes([IsAuthenticated])
class ContractSet(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('client__last_name', 'client__email', 'date_create', 'amount')

    def get_queryset(self):
        if self.request.user.team == 'MNG':
            return Contract.objects.all()
        else:
            return Contract.objects.filter(sale_contact=self.request.user)
