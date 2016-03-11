from rest_framework import serializers
from client.models import Load, DBChanges, Connection, Node, SyncGenerator, \
    Bus, Utility
from django.contrib.auth.models import User


class LoadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Load
        fields = ('id', 'operational_status', 'is_bus', 'latitude', 'longitude',
                  'name', 'power_rating', 'power_factor_percent',
                  'power_factor_type', 'min_PU_voltage', 'wiring',
                  'nominal_LL_voltage', 'a_voltage_magnitude',
                  'a_voltage_angle', 'a_voltage_PU', 'a_current_magnitude',
                  'a_current_angle', 'P', 'Q',  'created_date')


class SyncGeneratorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SyncGenerator
        fields = ('id', 'operational_status', 'is_bus', 'latitude', 'longitude',
                  'name', 'power_rating', 'LL_voltage', 'RPM_rating',
                  'pole_count', 'pf_percent', 'wiring', 'a_voltage_magnitude',
                  'a_voltage_angle', 'a_voltage_PU', 'a_current_magnitude',
                  'a_current_angle', 'P', 'Q',  'created_date')


class BusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bus
        fields = ('id', 'operational_status', 'is_bus', 'latitude', 'longitude',
                  'name', 'nominal_LL_voltage', 'a_voltage_magnitude',
                  'a_voltage_angle', 'a_voltage_PU', 'created_date')


class UtilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Utility
        fields = ('id', 'operational_status', 'is_bus', 'latitude', 'longitude',
                  'name', 'LL_voltage', 'voltage_angle',
                  'short_circuit_3_phase', 'short_circuit_SLG',
                  'x_r_ratio_positive', 'x_r_ratio_zero', 'x_positive',
                  'x_zero', 'r_positive', 'r_zero' 'a_voltage_magnitude',
                  'a_voltage_angle', 'a_voltage_PU', 'a_current_magnitude',
                  'a_current_angle', 'created_date')


class NodeListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Node
        fields = ('id', 'name', 'type')


class ConnectionListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Connection
        fields = ('id', 'from_id', 'to_id', 'type')


class DBChangesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DBChanges
        fields = ('update_check',)
