from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes
from rest_framework.utils import model_meta

from team_user.models import EpicUser


class TeamSerializer(ModelSerializer):
    class Meta:
        model = EpicUser
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'phone',
                  'date_joined',
                  'last_login',
                  'team',
                  'password']
        extra_kwargs = {'password': {'write_only': True},
                        'date_joined': {'read_only': True},
                        'last_login': {'read_only': True}}

    def update(self, instance, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(TeamSerializer, self).update(instance, validated_data)

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(TeamSerializer, self).create(validated_data)
