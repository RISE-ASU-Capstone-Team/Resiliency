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

    # Non-editable = 3
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
    from_id = models.IntegerField(default=0)
    to_id = models.IntegerField(default=0)
    type = models.IntegerField(default=0)
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

    # Non-editable = 13
    current_rating = models.FloatField(max_length=100, default=0.0)
    nominal_LL_voltage = models.FloatField(max_length=100, default=0.0)
    current_1_magnitude = models.FloatField(max_length=100, default=0.0)
    current_1_angle = models.FloatField(max_length=100, default=0.0)
    real_power = models.FloatField(max_length=100, default=0.0)
    reactive_power = models.FloatField(max_length=100, default=0.0)

    def __str__(self):
        return self.id


class SyncGenerator(Node):
    # Total Editable = 11
    stiffness = models.BooleanField(default=True)
    power_rating = models.FloatField(max_length=100, default=0.0)
    RPM_rating = models.IntegerField(default=0.0)
    number_of_poles = models.IntegerField(default=0.0)
    power_factor_percent = models.FloatField(max_length=100, default=0.0)
    wiring = models.IntegerField(default=0)

    # Non-editable
    nominal_LL_voltage = models.FloatField(max_length=100, default=0.0)
    current_1_magnitude = models.FloatField(max_length=100, default=0.0)
    current_1_angle = models.FloatField(max_length=100, default=0.0)
    real_power = models.FloatField(max_length=100, default=0.0)
    reactive_power = models.FloatField(max_length=100, default=0.0)

    def __str__(self):
        return self.id


class Bus(Node):
    # Total Editable = 3

    # Non-editable
    nominal_LL_voltage = models.FloatField(max_length=100, default=0.0)

    def __str__(self):
        return self.id


class Utility(models.Model):
    # Total Editable = 5
    base_power = models.FloatField(max_length=100, default=0.0)
    LL_voltage = models.FloatField(max_length=100, default=0.0)
    voltage_angle = models.FloatField(max_length=100, default=0.0)
    short_circuit_3_phase = models.FloatField(max_length=100, default=0.0)
    short_circuit_SLG = models.FloatField(max_length=100, default=0.0)
    stiffness = models.BooleanField(default=True)
    r_1 = models.FloatField(max_length=100, default=0.0)
    x_1 = models.FloatField(max_length=100, default=0.0)
    r_0 = models.FloatField(max_length=100, default=0.0)
    x_0 = models.FloatField(max_length=100, default=0.0)

    # Non-editable
    current_1_magnitude = models.FloatField(max_length=100, default=0.0)
    current_1_angle = models.FloatField(max_length=100, default=0.0)


class TwoWindingTransformer(models.Model):
    # Total Editable = 6
    operational_status = models.BooleanField(default=True)
    is_bus = models.BooleanField(default=True)
    latitude = models.FloatField(max_length=50, default=0)
    longitude = models.FloatField(max_length=50, default=0)
    from_bus = models.IntegerField(default=0)
    to_bus = models.IntegerField(default=0)

    name = models.CharField(max_length=100, default="Untitled TWTransformer")
    base_power = models.FloatField(max_length=100, default=0.0)

    created_date = models.BigIntegerField(default=time.time())

    def __str__(self):
        return self.name

'''
class Power(models.Model):
    operational_status = models.BooleanField(default=True)
    is_bus = models.BooleanField(default=True)
    latitude = models.FloatField(max_length=50, default=0)
    longitude = models.FloatField(max_length=50, default=0)
    created_date = models.BigIntegerField(default=time.time())

    def __str__(self):
        return self.id


class PowerArc(models.Model):
    operational_status = models.BooleanField(default=True)
    is_bus = models.BooleanField(default=True)
    from_bus = models.IntegerField(default=0)
    to_bus = models.IntegerField(default=0)

    def __str__(self):
        return self.id
'''

# ------------------------------------------------------------------ Water nodes
