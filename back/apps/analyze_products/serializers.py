from django.contrib.auth.models import Group, User
from rest_framework import serializers


class DataSerializer(serializers.Serializer):
    fields = '__all__'