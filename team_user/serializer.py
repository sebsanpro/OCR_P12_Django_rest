from rest_framework.serializers import ModelSerializer

from team_user.models import EpicUser


class TeamSerializer(ModelSerializer):
    class Meta:
        model = EpicUser
        fields = '__all__'
