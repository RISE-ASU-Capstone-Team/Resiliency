# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-25 22:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Untitled Connection', max_length=100)),
                ('operational_status', models.BooleanField(default=True)),
                ('current_1_magnitude', models.FloatField(default=0.0, max_length=100)),
                ('current_1_angle', models.FloatField(default=0.0, max_length=100)),
                ('real_power_entering', models.FloatField(default=0.0, max_length=100)),
                ('reactive_power_entering', models.FloatField(default=0.0, max_length=100)),
                ('real_power_leaving', models.FloatField(default=0.0, max_length=100)),
                ('reactive_power_leaving', models.FloatField(default=0.0, max_length=100)),
                ('type', models.IntegerField(default=0)),
                ('from_bus_id', models.IntegerField(default=-1)),
                ('to_bus_id', models.IntegerField(default=-1)),
                ('created_date', models.BigIntegerField(default=1458943908.3438962)),
            ],
        ),
        migrations.CreateModel(
            name='DBChanges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_check', models.BigIntegerField(default=1458943908.3438962)),
            ],
        ),
        migrations.CreateModel(
            name='LineCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Untitled Node', max_length=100)),
                ('r_1', models.FloatField(default=0, max_length=100)),
                ('x_1', models.FloatField(default=0, max_length=100)),
                ('r_0', models.FloatField(default=0, max_length=100)),
                ('x_0', models.FloatField(default=0, max_length=100)),
                ('continuous_ampacity', models.FloatField(default=0, max_length=100)),
                ('emergency_ampacity', models.FloatField(default=0, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Untitled Node', max_length=100)),
                ('operational_status', models.BooleanField(default=True)),
                ('is_bus', models.BooleanField(default=True)),
                ('voltage_1_magnitude', models.FloatField(default=0.0, max_length=100)),
                ('voltage_1_angle', models.FloatField(default=0.0, max_length=100)),
                ('voltage_1_PU', models.FloatField(default=0.0, max_length=100)),
                ('type', models.IntegerField(default=0)),
                ('latitude', models.FloatField(default=0)),
                ('longitude', models.FloatField(default=0)),
                ('created_date', models.BigIntegerField(default=1458943908.3438962)),
            ],
        ),
        migrations.CreateModel(
            name='Power',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature_units', models.IntegerField(default=0)),
                ('ambient_temp_celsius', models.FloatField(default=0, max_length=100)),
                ('ambient_temp_fahrenheit', models.FloatField(default=0, max_length=100)),
                ('voltage_units', models.IntegerField(default=0)),
                ('current_units', models.IntegerField(default=0)),
                ('power_units', models.IntegerField(default=0)),
                ('base_frequency', models.IntegerField(default=0)),
                ('bus_count', models.IntegerField(default=0)),
                ('utility_count', models.IntegerField(default=0)),
                ('generator_count', models.IntegerField(default=0)),
                ('load_count', models.IntegerField(default=0)),
                ('transformer_count', models.IntegerField(default=0)),
                ('branch_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='WireData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Untitled Node', max_length=100)),
                ('phase_resistance_50_C', models.FloatField(default=0, max_length=100)),
                ('phase_GMR', models.FloatField(default=0, max_length=100)),
                ('phase_continuous_ampacity', models.FloatField(default=0, max_length=100)),
                ('phase_emergency_ampacity', models.FloatField(default=0, max_length=100)),
                ('phase_diameter', models.FloatField(default=0, max_length=100)),
                ('neutral_resistance_50_C', models.FloatField(default=0, max_length=100)),
                ('neutral_GMR', models.FloatField(default=0, max_length=100)),
                ('neutral_continuous_ampacity', models.FloatField(default=0, max_length=100)),
                ('neutral_emergency_ampacity', models.FloatField(default=0, max_length=100)),
                ('neutral_diameter', models.FloatField(default=0, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('node_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='client.Node')),
                ('nominal_LL_voltage', models.FloatField(default=0.0, max_length=100)),
            ],
            bases=('client.node',),
        ),
        migrations.CreateModel(
            name='Cable',
            fields=[
                ('connection_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='client.Connection')),
                ('linecode_object_id', models.IntegerField(default=0)),
                ('voltage_rating', models.FloatField(default=0.0, max_length=100)),
                ('length', models.FloatField(default=0.0, max_length=100)),
                ('number_of_cables', models.IntegerField(default=0)),
            ],
            bases=('client.connection',),
        ),
        migrations.CreateModel(
            name='DirectConnection',
            fields=[
                ('connection_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='client.Connection')),
                ('from_bus_voltage_rating', models.FloatField(default=0.0, max_length=100)),
                ('to_bus_voltage_rating', models.FloatField(default=0.0, max_length=100)),
            ],
            bases=('client.connection',),
        ),
        migrations.CreateModel(
            name='Load',
            fields=[
                ('node_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='client.Node')),
                ('power_rating', models.FloatField(default=0.0, max_length=100)),
                ('power_factor_percent', models.FloatField(default=0.0, max_length=100)),
                ('power_factor_type', models.IntegerField(default=0)),
                ('min_PU_voltage', models.FloatField(default=0.0, max_length=100)),
                ('wiring', models.IntegerField(default=0)),
                ('load_model', models.IntegerField(default=0)),
                ('current_rating', models.FloatField(default=0.0, max_length=100)),
                ('nominal_LL_voltage', models.FloatField(default=0.0, max_length=100)),
                ('current_1_magnitude', models.FloatField(default=0.0, max_length=100)),
                ('current_1_angle', models.FloatField(default=0.0, max_length=100)),
                ('real_power', models.FloatField(default=0.0, max_length=100)),
                ('reactive_power', models.FloatField(default=0.0, max_length=100)),
            ],
            bases=('client.node',),
        ),
        migrations.CreateModel(
            name='OverheadLine',
            fields=[
                ('connection_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='client.Connection')),
                ('wiredata_object_id', models.IntegerField(default=0)),
                ('number_of_conductors', models.IntegerField(default=0)),
                ('length', models.FloatField(default=0.0, max_length=100)),
                ('soil_resistivity', models.FloatField(default=0.0, max_length=100)),
                ('kron_reduction', models.BooleanField(default=True)),
                ('x_1_coordinate', models.FloatField(default=0.0, max_length=100)),
                ('x_2_coordinate', models.FloatField(default=0.0, max_length=100)),
                ('x_3_coordinate', models.FloatField(default=0.0, max_length=100)),
                ('y_1_coordinate', models.FloatField(default=0.0, max_length=100)),
                ('y_2_coordinate', models.FloatField(default=0.0, max_length=100)),
                ('y_3_coordinate', models.FloatField(default=0.0, max_length=100)),
                ('h_1_coordinate', models.FloatField(default=0.0, max_length=100)),
                ('h_2_coordinate', models.FloatField(default=0.0, max_length=100)),
                ('h_3_coordinate', models.FloatField(default=0.0, max_length=100)),
                ('x_4_coordinate', models.FloatField(default=0.0, max_length=100)),
                ('y_4_coordinate', models.FloatField(default=0.0, max_length=100)),
                ('h_4_coordinate', models.FloatField(default=0.0, max_length=100)),
                ('nominal_LL_voltage', models.FloatField(default=0.0, max_length=100)),
            ],
            bases=('client.connection',),
        ),
        migrations.CreateModel(
            name='SyncGenerator',
            fields=[
                ('node_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='client.Node')),
                ('stiffness', models.BooleanField(default=True)),
                ('power_rating', models.FloatField(default=0.0, max_length=100)),
                ('RPM_rating', models.IntegerField(default=0.0)),
                ('number_of_poles', models.IntegerField(default=0.0)),
                ('power_factor_percent', models.FloatField(default=0.0, max_length=100)),
                ('wiring', models.IntegerField(default=0)),
                ('nominal_LL_voltage', models.FloatField(default=0.0, max_length=100)),
                ('current_1_magnitude', models.FloatField(default=0.0, max_length=100)),
                ('current_1_angle', models.FloatField(default=0.0, max_length=100)),
                ('real_power', models.FloatField(default=0.0, max_length=100)),
                ('reactive_power', models.FloatField(default=0.0, max_length=100)),
            ],
            bases=('client.node',),
        ),
        migrations.CreateModel(
            name='TwoWindingTransformer',
            fields=[
                ('connection_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='client.Connection')),
                ('from_bus_voltage_rating', models.FloatField(default=0.0, max_length=100)),
                ('to_bus_voltage_rating', models.FloatField(default=0.0, max_length=100)),
                ('from_bus_wiring', models.IntegerField(default=0)),
                ('to_bus_wiring', models.IntegerField(default=0)),
                ('power_rating', models.FloatField(default=0.0, max_length=100)),
                ('x_percent', models.FloatField(default=0.0, max_length=100)),
                ('r_percent', models.FloatField(default=0.0, max_length=100)),
                ('tap_percent', models.FloatField(default=0.0, max_length=100)),
                ('tap_side', models.BooleanField(default=True)),
                ('min_tap', models.FloatField(default=0.0, max_length=100)),
                ('max_tap', models.FloatField(default=0.0, max_length=100)),
            ],
            bases=('client.connection',),
        ),
        migrations.CreateModel(
            name='Utility',
            fields=[
                ('node_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='client.Node')),
                ('base_power', models.FloatField(default=0.0, max_length=100)),
                ('LL_voltage', models.FloatField(default=0.0, max_length=100)),
                ('voltage_angle', models.FloatField(default=0.0, max_length=100)),
                ('short_circuit_3_phase', models.FloatField(default=0.0, max_length=100)),
                ('short_circuit_SLG', models.FloatField(default=0.0, max_length=100)),
                ('stiffness', models.BooleanField(default=True)),
                ('r_1', models.FloatField(default=0.0, max_length=100)),
                ('x_1', models.FloatField(default=0.0, max_length=100)),
                ('r_0', models.FloatField(default=0.0, max_length=100)),
                ('x_0', models.FloatField(default=0.0, max_length=100)),
                ('current_1_magnitude', models.FloatField(default=0.0, max_length=100)),
                ('current_1_angle', models.FloatField(default=0.0, max_length=100)),
            ],
            bases=('client.node',),
        ),
    ]
