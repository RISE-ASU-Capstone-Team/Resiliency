from rest_framework import serializers
from client.models import Load, DBChanges, Connection, Node, SyncGenerator, \
    Bus, Utility, TwoWindingTransformer, DirectConnection, Cable, OverheadLine,\
    Power, WireData, LineCode, Reservoir, Pipe
from django.contrib.auth.models import User


class NodeMarkerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Node
        fields = ('id', 'name', 'type', 'latitude', 'longitude')


class ConnectionListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Connection
        fields = ('id', 'name','from_bus_id', 'to_bus_id', 'type')


# ------------------------------------------------------------------- Power Node
class LoadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Load
        fields = ('id', 'operational_status', 'name', 'latitude',
                  'longitude', 'type', 'power_rating',
                  'power_factor_percent', 'power_factor_type', 'min_PU_voltage',
                  'wiring', 'load_model', 'current_rating', 'nominal_voltage',
                  'LL_voltage', 'voltage_1_magnitude', 'voltage_1_angle',
                  'voltage_1_PU', 'current_1_magnitude', 'current_1_angle',
                  'real_power', 'reactive_power', 'created_date')


class SyncGeneratorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SyncGenerator
        fields = ('id', 'operational_status', 'name', 'latitude',
                  'longitude', 'type', 'stiffness', 'power_rating',
                  'RPM_rating', 'number_of_poles', 'power_factor_percent',
                  'wiring', 'nominal_voltage', 'LL_voltage',
                  'voltage_1_magnitude', 'voltage_1_angle', 'voltage_1_PU',
                  'current_1_magnitude', 'current_1_angle', 'real_power',
                  'reactive_power', 'created_date')


class BusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bus
        fields = ('id', 'operational_status', 'name', 'latitude',
                  'longitude', 'type', 'nominal_voltage', 'LL_voltage',
                  'voltage_1_magnitude', 'voltage_1_angle', 'voltage_1_PU',
                  'created_date')


class UtilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Utility
        fields = ('id', 'operational_status', 'type', 'name',
                  'latitude', 'longitude', 'base_power', 'nominal_voltage',
                  'voltage_angle', 'short_circuit_3_phase', 'short_circuit_SLG',
                  'stiffness', 'r_1', 'x_1', 'r_0', 'x_0', 'LL_voltage',
                  'voltage_1_magnitude', 'voltage_1_angle', 'voltage_1_PU',
                  'current_1_magnitude', 'current_1_angle', 'created_date')


# ------------------------------------------------------------- Power Connection
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
                  'voltage_rating', 'length',
                  'number_of_cables', 'from_bus_id', 'to_bus_id',
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
                  'x_3_coordinate', 'h_1_coordinate', 'h_2_coordinate',
                  'h_3_coordinate', 'x_4_coordinate',
                  'h_4_coordinate', 'from_bus_id', 'to_bus_id',
                  'type', 'nominal_LL_voltage', 'current_1_magnitude',
                  'current_1_angle', 'real_power_entering',
                  'reactive_power_entering', 'real_power_leaving',
                  'reactive_power_leaving', 'created_date')


# ------------------------------------------------------------------- Power Info
class PowerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Power
        fields = ('bus_count', 'utility_count',
                  'generator_count', 'load_count', 'transformer_count',
                  'branch_count')


class WireDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WireData
        fields = ('id', 'name', 'type',
                  'wire_type', 'resistance_50_C', 'GMR',
                  'continuous_ampacity', 'emergency_ampacity', 'diameter')


class LineCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LineCode
        fields = ('id', 'name', 'r_1',
                  'x_1', 'r_0', 'x_0',
                  'continuous_ampacity', 'emergency_ampacity')


# ------------------------------------------------------------------ Water Nodes
class ReservoirSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reservoir
        fields = ('id', 'operational_status', 'name', 'latitude',
                  'longitude', 'type', 'created_date', 'elevation',
                  'net_inflow', 'water_age')


# ------------------------------------------------------------ Water Connections
class PipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pipe
        fields = ('id', 'operational_status', 'name', 'from_bus_id', 'to_bus_id',
                'type', 'created_date', 'diameter', 'flow', 'velocity', 'quality')


# -------------------------------------------------------------------- DB Change
class DBChangesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DBChanges
        fields = ('update_check',)
