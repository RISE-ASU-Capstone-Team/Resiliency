from django.db import models
import time


# Create your models here.
class DBChanges(models.Model):
    update_check = models.BigIntegerField(default=time.time())

    def __str__(self):
        return self.id


# ------------------------------------------------------------------------ Nodes
class Node(models.Model):
    # Total editable = 3
    name = models.CharField(max_length=100, default="Untitled Node")
    operational_status = models.BooleanField(default=True)
    is_bus = models.BooleanField(default=True)

    # Non-editable = 9
    nominal_voltage = models.FloatField(max_length=100, default=0.0)
    LL_voltage = models.FloatField(max_length=100, default=0.0)
    voltage_1_magnitude = models.FloatField(max_length=100, default=0.0)
    voltage_1_angle = models.FloatField(max_length=100, default=0.0)
    voltage_1_PU = models.FloatField(max_length=100, default=0.0)
    type = models.IntegerField(default=0)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    created_date = models.BigIntegerField(default=time.time())

    def __str__(self):
        return self.id


# ------------------------------------------------------------------ Connections
class Connection(models.Model):
    # Total editable = 2
    name = models.CharField(max_length=100, default="Untitled Connection")
    operational_status = models.BooleanField(default=True)

    # Non-editable = 10
    current_1_magnitude = models.FloatField(max_length=100, default=0.0)
    current_1_angle = models.FloatField(max_length=100, default=0.0)
    real_power_entering = models.FloatField(max_length=100, default=0.0)
    reactive_power_entering = models.FloatField(max_length=100, default=0.0)
    real_power_leaving = models.FloatField(max_length=100, default=0.0)
    reactive_power_leaving = models.FloatField(max_length=100, default=0.0)
    type = models.IntegerField(default=0)
    from_bus_id = models.IntegerField(default=-1)
    to_bus_id = models.IntegerField(default=-1)
    created_date = models.BigIntegerField(default=time.time())

    def __str__(self):
        return self.id


# ------------------------------------------------------------------ Power nodes
class Load(Node):
    # Total editable = 9
    power_rating = models.FloatField(max_length=100, default=0.0)
    power_factor_percent = models.FloatField(max_length=100, default=0.0)
    power_factor_type = models.IntegerField(default=0)
    min_PU_voltage = models.FloatField(max_length=100, default=0.0)
    wiring = models.IntegerField(default=0)
    load_model = models.IntegerField(default=0)

    # Non-editable = 14
    current_rating = models.FloatField(max_length=100, default=0.0)
    current_1_magnitude = models.FloatField(max_length=100, default=0.0)
    current_1_angle = models.FloatField(max_length=100, default=0.0)
    real_power = models.FloatField(max_length=100, default=0.0)
    reactive_power = models.FloatField(max_length=100, default=0.0)

    def __str__(self):
        return self.id


class SyncGenerator(Node):
    # Total Editable = 9
    stiffness = models.BooleanField(default=True)
    power_rating = models.FloatField(max_length=100, default=0.0)
    RPM_rating = models.IntegerField(default=0.0)
    number_of_poles = models.IntegerField(default=0.0)
    power_factor_percent = models.FloatField(max_length=100, default=0.0)
    wiring = models.IntegerField(default=0)

    # Non-editable = 13
    current_1_magnitude = models.FloatField(max_length=100, default=0.0)
    current_1_angle = models.FloatField(max_length=100, default=0.0)
    real_power = models.FloatField(max_length=100, default=0.0)
    reactive_power = models.FloatField(max_length=100, default=0.0)

    def __str__(self):
        return self.id


class Bus(Node):
    # Total Editable = 3

    # Non-editable = 9

    def __str__(self):
        return self.id


class Utility(Node):
    # Total Editable = 13
    base_power = models.FloatField(max_length=100, default=0.0)
    voltage_angle = models.FloatField(max_length=100, default=0.0)
    short_circuit_3_phase = models.FloatField(max_length=100, default=0.0)
    short_circuit_SLG = models.FloatField(max_length=100, default=0.0)
    stiffness = models.BooleanField(default=True)
    r_1 = models.FloatField(max_length=100, default=0.0)
    x_1 = models.FloatField(max_length=100, default=0.0)
    r_0 = models.FloatField(max_length=100, default=0.0)
    x_0 = models.FloatField(max_length=100, default=0.0)

    # Non-editable = 11
    current_1_magnitude = models.FloatField(max_length=100, default=0.0)
    current_1_angle = models.FloatField(max_length=100, default=0.0)

    def __str__(self):
        return self.id


# ------------------------------------------------------------ Power Connections
class TwoWindingTransformer(Connection):
    # Total Editable = 10
    from_bus_voltage_rating = models.FloatField(max_length=100, default=0.0)
    to_bus_voltage_rating = models.FloatField(max_length=100, default=0.0)
    from_bus_wiring = models.IntegerField(default=0)
    to_bus_wiring = models.IntegerField(default=0)
    power_rating = models.FloatField(max_length=100, default=0.0)
    x_percent = models.FloatField(max_length=100, default=0.0)
    r_percent = models.FloatField(max_length=100, default=0.0)
    tap_percent = models.FloatField(max_length=100, default=0.0)
    tap_side = models.BooleanField(default=True)
    min_tap = models.FloatField(max_length=100, default=0.0)
    max_tap = models.FloatField(max_length=100, default=0.0)

    def __str__(self):
        return self.id


class DirectConnection(Connection):
    # Total Editable = 2

    # Non-Editable = 9
    from_bus_voltage_rating = models.FloatField(max_length=100, default=0.0)
    to_bus_voltage_rating = models.FloatField(max_length=100, default=0.0)

    def __str__(self):
        return self.id


class Cable(Connection):
    # Total Editable = 6
    linecode_object_id = models.IntegerField(default=0)
    voltage_rating = models.FloatField(max_length=100, default=0.0)
    length = models.FloatField(max_length=100, default=0.0)
    number_of_cables = models.IntegerField(default=0)

    # Non-Editable = 7

    def __str__(self):
        return self.id


class OverheadLine(Connection):
    # Total Editable = 6
    wiredata_object_id = models.IntegerField(default=1)
    number_of_conductors = models.IntegerField(default=0)
    length = models.FloatField(max_length=100, default=0.0)
    soil_resistivity = models.FloatField(max_length=100, default=0.0)
    kron_reduction = models.BooleanField(default=True)
    x_1_coordinate = models.FloatField(max_length=100, default=0.0)
    x_2_coordinate = models.FloatField(max_length=100, default=0.0)
    x_3_coordinate = models.FloatField(max_length=100, default=0.0)
    y_1_coordinate = models.FloatField(max_length=100, default=0.0)
    y_2_coordinate = models.FloatField(max_length=100, default=0.0)
    y_3_coordinate = models.FloatField(max_length=100, default=0.0)
    h_1_coordinate = models.FloatField(max_length=100, default=0.0)
    h_2_coordinate = models.FloatField(max_length=100, default=0.0)
    h_3_coordinate = models.FloatField(max_length=100, default=0.0)

    # Optional inputs = 3
    x_4_coordinate = models.FloatField(max_length=100, default=0.0)
    y_4_coordinate = models.FloatField(max_length=100, default=0.0)
    h_4_coordinate = models.FloatField(max_length=100, default=0.0)

    # Non-Editable = 8
    nominal_LL_voltage = models.FloatField(max_length=100, default=0.0)

    def __str__(self):
        return self.id


# ------------------------------------------------------------------- Power Info
class Power(models.Model):
    temperature_units = models.IntegerField(default=0)
    ambient_temp_celsius = models.FloatField(max_length=100, default=0)
    ambient_temp_fahrenheit = models.FloatField(max_length=100, default=0)
    voltage_units = models.IntegerField(default=0)
    current_units = models.IntegerField(default=0)
    power_units = models.IntegerField(default=0)
    base_frequency = models.IntegerField(default=0)
    bus_count = models.IntegerField(default=0)
    utility_count = models.IntegerField(default=0)
    generator_count = models.IntegerField(default=0)
    load_count = models.IntegerField(default=0)
    transformer_count = models.IntegerField(default=0)
    branch_count = models.IntegerField(default=0)

    def __str__(self):
        return self.id


class WireData(models.Model):
    # Editable: 8
    name = models.CharField(max_length=100, default="Untitled Wire")
    type = models.CharField(max_length=100, default="Unknown Type")
    wire_type = models.IntegerField(default=0)
    resistance_50_C = models.FloatField(max_length=100, default=0)
    GMR = models.FloatField(max_length=100, default=0)
    continuous_ampacity = models.FloatField(max_length=100, default=0)
    emergency_ampacity = models.FloatField(max_length=100, default=0)
    diameter = models.FloatField(max_length=100, default=0)


class LineCode(models.Model):
    name = models.CharField(max_length=100, default="Untitled Line")
    r_1 = models.FloatField(max_length=100, default=0)
    x_1 = models.FloatField(max_length=100, default=0)
    r_0 = models.FloatField(max_length=100, default=0)
    x_0 = models.FloatField(max_length=100, default=0)
    continuous_ampacity = models.FloatField(max_length=100, default=0)
    emergency_ampacity = models.FloatField(max_length=100, default=0)

# ------------------------------------------------------------------ Water nodes
class Reservoir(Node):
    # Total editable = 3
    elevation = models.FloatField(max_length=100, default=0.0)
    net_inflow = models.FloatField(max_length=100, default=0.0)
    water_age = models.FloatField(max_length=100, default=0)

    def __str__(self):
        return self.id

# ------------------------------------------------------------------ Water Connections
class Pipe(Connection):
    # Total Editable = 4
    diameter = models.FloatField(max_length=100, default=0.0)
    flow = models.FloatField(max_length=100, default=0.0)
    velocity = models.FloatField(max_length=100, default=0.0)
    quality = models.FloatField(max_length=100, default=0.0)

    # Non-Editable = 0

    def __str__(self):
        return self.id
