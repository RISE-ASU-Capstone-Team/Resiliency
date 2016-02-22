from rest_framework import serializers
from client.models import Power, DBChanges
from django.contrib.auth.models import User


class PowerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Power
        fields = ('id', 'name', 'active', 'type', 'latitude', 'longitude',
                  'created_date')


class PowerListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Power
        fields = ('id', 'name')


class DBChangesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DBChanges
        fields = ('update_check',)
