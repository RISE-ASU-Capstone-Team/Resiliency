from django.db import models
import time


# Create your models here.
class DBChanges(models.Model):
    update_check = models.BigIntegerField(default=time.time())

    def __str__(self):
        return self.id


# ------------------------------------------------------------------------ Nodes
class Node(models.Model):
    name = models.CharField(max_length=100, default="UN")
    f_id = models.IntegerField(default=0)
    type = models.IntegerField(default=0)


# ------------------------------------------------------------------ Connections
class Connection(models.Model):
    from_id = models.IntegerField(default=0)
    to_id = models.IntegerField(default=0)
    type = models.IntegerField(default=0)
    created_date = models.BigIntegerField(default=time.time())

    def __str__(self):
        return self.id


# ------------------------------------------------------------------ Power nodes
class Load(models.Model):
    # Total editable = 13
    operational_status = models.BooleanField(default=True)
    is_bus = models.BooleanField(default=True)
    latitude = models.FloatField(max_length=50, default=0)
    longitude = models.FloatField(max_length=50, default=0)

    name = models.CharField(max_length=100, default="Untitled Load")
    voltage_rating = models.FloatField(max_length=100, default=0.0)
    current_rating = models.FloatField(max_length=100, default=0.0)
    power_rating = models.FloatField(max_length=100, default=0.0)
    power_factor_percent = models.FloatField(max_length=100, default=0.0)
    power_factor_type = models.IntegerField(default=0)
    min_PU_voltage = models.FloatField(max_length=100, default=0.0)
    wiring = models.IntegerField(default=0)
    load_model = models.IntegerField(default=0)

    # Non-editable
    nominal_LL_voltage = models.FloatField(max_length=100, default=0.0)
    a_voltage_magnitude = models.FloatField(max_length=100, default=0.0)
    a_voltage_angle = models.FloatField(max_length=100, default=0.0)
    a_voltage_PU = models.FloatField(max_length=100, default=0.0)
    a_current_magnitude = models.FloatField(max_length=100, default=0.0)
    a_current_angle = models.FloatField(max_length=100, default=0.0)
    P = models.FloatField(max_length=100, default=0.0)
    Q = models.FloatField(max_length=100, default=0.0)
    created_date = models.BigIntegerField(default=time.time())

    def __str__(self):
        return self.name


class SyncGenerator(models.Model):
    # Total Editable = 11
    operational_status = models.BooleanField(default=True)
    is_bus = models.BooleanField(default=True)
    latitude = models.FloatField(max_length=50, default=0)
    longitude = models.FloatField(max_length=50, default=0)

    name = models.CharField(max_length=100, default="Untitled Sync Gen")
    power_rating = models.FloatField(max_length=100, default=0.0)
    LL_voltage = models.FloatField(max_length=100, default=0.0)
    RPM_rating = models.IntegerField(default=0.0)
    pole_count = models.IntegerField(default=0.0)
    pf_percent = models.FloatField(max_length=100, default=0.0)
    wiring = models.IntegerField(default=0)

    # Non-editable
    a_voltage_magnitude = models.FloatField(max_length=100, default=0.0)
    a_voltage_angle = models.FloatField(max_length=100, default=0.0)
    a_voltage_PU = models.FloatField(max_length=100, default=0.0)
    a_current_magnitude = models.FloatField(max_length=100, default=0.0)
    a_current_angle = models.FloatField(max_length=100, default=0.0)
    P = models.FloatField(max_length=100, default=0.0)
    Q = models.FloatField(max_length=100, default=0.0)
    created_date = models.BigIntegerField(default=time.time())

    def __str__(self):
        return self.name


class Bus(models.Model):
    # Total Editable = 5
    operational_status = models.BooleanField(default=True)
    is_bus = models.BooleanField(default=True)
    latitude = models.FloatField(max_length=50, default=0)
    longitude = models.FloatField(max_length=50, default=0)

    name = models.CharField(max_length=100, default="Untitled Bus")

    # Non-editable
    nominal_LL_voltage = models.FloatField(max_length=100, default=0.0)
    a_voltage_magnitude = models.FloatField(max_length=100, default=0.0)
    a_voltage_angle = models.FloatField(max_length=100, default=0.0)
    a_voltage_PU = models.FloatField(max_length=100, default=0.0)
    created_date = models.BigIntegerField(default=time.time())

    def __str__(self):
        return self.name


class Utility(models.Model):
    # Total Editable = 5
    operational_status = models.BooleanField(default=True)
    is_bus = models.BooleanField(default=True)
    latitude = models.FloatField(max_length=50, default=0)
    longitude = models.FloatField(max_length=50, default=0)

    name = models.CharField(max_length=100, default="Untitled Utility")
    LL_voltage = models.FloatField(max_length=100, default=0.0)
    voltage_angle = models.FloatField(max_length=100, default=0.0)
    short_circuit_3_phase = models.FloatField(max_length=100, default=0.0)
    short_circuit_SLG = models.FloatField(max_length=100, default=0.0)
    x_r_ratio_positive = models.FloatField(max_length=100, default=0.0)
    x_r_ratio_zero = models.FloatField(max_length=100, default=0.0)
    x_positive = models.FloatField(max_length=100, default=0.0)
    x_zero = models.FloatField(max_length=100, default=0.0)

    # Non-editable
    r_positive = models.FloatField(max_length=100, default=0.0)
    r_zero = models.FloatField(max_length=100, default=0.0)
    a_voltage_magnitude = models.FloatField(max_length=100, default=0.0)
    a_voltage_angle = models.FloatField(max_length=100, default=0.0)
    a_voltage_PU = models.FloatField(max_length=100, default=0.0)
    a_current_magnitude = models.FloatField(max_length=100, default=0.0)
    a_current_angle = models.FloatField(max_length=100, default=0.0)
    created_date = models.BigIntegerField(default=time.time())


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

