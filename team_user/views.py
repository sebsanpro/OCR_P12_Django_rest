from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from team_user.models import EpicUser
from team_user.serializers import TeamSerializer


@permission_classes([IsAuthenticated])
class TeamSet(viewsets.ModelViewSet):
    queryset = EpicUser.objects.all()
    serializer_class = TeamSerializer
