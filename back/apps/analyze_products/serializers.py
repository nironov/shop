from django.contrib.auth.models import Group, User
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer


class DataSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'data': instance
        }