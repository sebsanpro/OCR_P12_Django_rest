from rest_framework import viewsets

from team_user.models import EpicUser
from team_user.serializers import TeamSerializer


class TeamSet(viewsets.ModelViewSet):
    queryset = EpicUser.objects.all()
    serializer_class = TeamSerializer
