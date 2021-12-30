from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from team_user.models import EpicUser
from team_user.serializer import TeamSerializer


class TeamSet(viewsets.ModelViewSet):
    queryset = EpicUser.objects.all()
    serializer_class = TeamSerializer
