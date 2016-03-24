from rest_framework import serializers
from client.models import Load, DBChanges, Connection, Node, SyncGenerator, \
    Bus, Utility, TwoWindingTransformer, DirectConnection, Cable, OverheadLine
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
        fields = ('id', 'operational_status', 'is_bus', 'type', 'name',
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
        fields = ('id', 'from_bus_id', 'to_bus_id', 'type')


class TwoWindingTransformerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TwoWindingTransformer
        fields = ('id', 'operational_status', 'name', 'from_bus_voltage_rating',
                  'to_bus_voltage_rating', 'from_bus_wiring', 'to_bus_wiring',
                  'power_rating', 'x_percent', 'r_percent', 'tap_percent',
                  'tap_side', 'min_tap', 'max_tap', 'from_bus_id', 'to_bus_id',
                  'type',  'name', 'current_1_magnitude', 'current_1_angle',
                  'real_power_entering', 'reactive_power_entering',
                  'real_power_leaving', 'reactive_power_leaving',
                  'created_date')


class DirectConnectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DirectConnection
        fields = ('id', 'operational_status', 'name', 'from_bus_voltage_rating',
                  'to_bus_voltage_rating', 'from_bus_id', 'to_bus_id',
                  'type', 'current_1_magnitude', 'current_1_angle',
                  'real_power_entering', 'reactive_power_entering',
                  'real_power_leaving', 'reactive_power_leaving',
                  'created_date')


class CableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cable
        fields = ('id', 'operational_status', 'name', 'linecode_object_id',
                  'voltage_rating', 'length', 'soil_resistivity',
                  'kron_reduction', 'from_bus_id', 'to_bus_id',
                  'type', 'current_1_magnitude', 'current_1_angle',
                  'real_power_entering', 'reactive_power_entering',
                  'real_power_leaving', 'reactive_power_leaving',
                  'created_date')


class OverheadLineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OverheadLine
        fields = ('id', 'operational_status', 'name', 'wiredata_object_id',
                  'number_of_conductors', 'length', 'soil_resistivity',
                  'kron_reduction', 'x_1_coordinate', 'x_2_coordinate',
                  'x_3_coordinate', 'y_1_coordinate', 'y_2_coordinate',
                  'y_3_coordinate', 'h_1_coordinate', 'h_2_coordinate',
                  'h_3_coordinate', 'x_4_coordinate', 'y_4_coordinate',
                  'h_4_coordinate', 'from_bus_id', 'to_bus_id',
                  'type', 'nominal_LL_voltage', 'current_1_magnitude',
                  'current_1_angle', 'real_power_entering',
                  'reactive_power_entering', 'real_power_leaving',
                  'reactive_power_leaving', 'created_date')


class DBChangesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DBChanges
        fields = ('update_check',)
