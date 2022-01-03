from rest_framework.serializers import ModelSerializer

from contract.serializers import ContractSerializer
from event.models import Event


class EventSerializer(ModelSerializer):
    contract_view = ContractSerializer(read_only=True)

    class Meta:
        model = Event
        fields = [field.name for field in model._meta.fields]
        fields.append('contract_view')
