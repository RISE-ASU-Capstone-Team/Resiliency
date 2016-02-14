from rest_framework import serializers
from client.models import Power
from django.contrib.auth.models import User


class PowerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Power
        fields = ('id', 'name', 'type', 'latitude', 'longitude', 'created_date')
