from rest_framework.serializers import ModelSerializer

from client.serializers import ClientSerializer
from contract.models import Contract


class ContractSerializer(ModelSerializer):
    client_view = ClientSerializer(read_only=True)

    class Meta:
        model = Contract
        fields = [field.name for field in model._meta.fields]
        fields.append('client_view')
        extra_kwargs = {'date_joined': {'read_only': True},
                        'last_login': {'read_only': True}}
