from rest_framework import serializers
from client.models import Load, DBChanges, Connection, Node, SyncGenerator, \
    Bus, Utility
from django.contrib.auth.models import User


class LoadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Load
        fields = ('id', 'operational_status', 'is_bus', 'name', 'latitude',
                  'longitude', 'type', 'power_rating',
                  'power_factor_percent', 'power_factor_type', 'min_PU_voltage',
                  'wiring', 'load_model', 'current_rating', 'nominal_LL_voltage',
                  'voltage_1_magnitude', 'voltage_1_angle', 'voltage_1_PU',
                  'current_1_magnitude', 'current_1_angle', 'real_power',
                  'reactive_power', 'created_date')


class SyncGeneratorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SyncGenerator
        fields = ('id', 'operational_status', 'is_bus', 'name', 'latitude',
                  'longitude', 'type', 'stiffness', 'power_rating',
                  'RPM_rating', 'number_of_poles', 'power_factor_percent',
                  'wiring', 'voltage_1_magnitude', 'voltage_1_angle',
                  'voltage_1_PU', 'current_1_magnitude', 'current_1_angle',
                  'real_power', 'reactive_power', 'created_date')


class BusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bus
        fields = ('id', 'operational_status', 'is_bus', 'latitude', 'longitude',
                  'name', 'type', 'nominal_LL_voltage', 'voltage_1_magnitude',
                  'voltage_1_angle', 'voltage_1_PU', 'created_date')


class UtilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Utility
        fields = ('id', 'operational_status', 'is_bus', 'name',
                  'latitude', 'longitude', 'base_power', 'LL_voltage',
                  'voltage_angle', 'short_circuit_3_phase', 'short_circuit_SLG',
                  'stiffness', 'r_1', 'x_1', 'r_0', 'x_0',
                  'voltage_1_magnitude', 'voltage_1_angle', 'voltage_1_PU',
                  'current_1_magnitude', 'current_1_angle', 'created_date')


class NodeMarkerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Node
        fields = ('id', 'name', 'type', 'latitude', 'longitude')


class ConnectionListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Connection
        fields = ('id', 'from_id', 'to_id', 'type')


class DBChangesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DBChanges
        fields = ('update_check',)
