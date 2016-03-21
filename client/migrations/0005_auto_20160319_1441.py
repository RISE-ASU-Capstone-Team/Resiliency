# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-19 21:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20160314_1244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='load',
            old_name='a_current_angle',
            new_name='current_1_angle',
        ),
        migrations.RenameField(
            model_name='load',
            old_name='a_current_magnitude',
            new_name='current_1_magnitude',
        ),
        migrations.RenameField(
            model_name='load',
            old_name='P',
            new_name='reactive_power',
        ),
        migrations.RenameField(
            model_name='load',
            old_name='Q',
            new_name='real_power',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='a_voltage_PU',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='a_voltage_angle',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='a_voltage_magnitude',
        ),
        migrations.RemoveField(
            model_name='load',
            name='a_voltage_PU',
        ),
        migrations.RemoveField(
            model_name='load',
            name='a_voltage_angle',
        ),
        migrations.RemoveField(
            model_name='load',
            name='a_voltage_magnitude',
        ),
        migrations.RemoveField(
            model_name='load',
            name='id',
        ),
        migrations.RemoveField(
            model_name='load',
            name='is_bus',
        ),
        migrations.RemoveField(
            model_name='load',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='load',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='load',
            name='name',
        ),
        migrations.RemoveField(
            model_name='load',
            name='operational_status',
        ),
        migrations.RemoveField(
            model_name='load',
            name='voltage_rating',
        ),
        migrations.RemoveField(
            model_name='syncgenerator',
            name='a_voltage_PU',
        ),
        migrations.RemoveField(
            model_name='syncgenerator',
            name='a_voltage_angle',
        ),
        migrations.RemoveField(
            model_name='syncgenerator',
            name='a_voltage_magnitude',
        ),
        migrations.RemoveField(
            model_name='utility',
            name='a_voltage_PU',
        ),
        migrations.RemoveField(
            model_name='utility',
            name='a_voltage_angle',
        ),
        migrations.RemoveField(
            model_name='utility',
            name='a_voltage_magnitude',
        ),
        migrations.AddField(
            model_name='load',
            name='node_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='client.Node'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='node',
            name='is_bus',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='node',
            name='operational_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='node',
            name='voltage_1_PU',
            field=models.FloatField(default=0.0, max_length=100),
        ),
        migrations.AddField(
            model_name='node',
            name='voltage_1_angle',
            field=models.FloatField(default=0.0, max_length=100),
        ),
        migrations.AddField(
            model_name='node',
            name='voltage_1_magnitude',
            field=models.FloatField(default=0.0, max_length=100),
        ),
        migrations.AlterField(
            model_name='bus',
            name='created_date',
            field=models.BigIntegerField(default=1458423253.0254164),
        ),
        migrations.AlterField(
            model_name='connection',
            name='created_date',
            field=models.BigIntegerField(default=1458423253.0234141),
        ),
        migrations.AlterField(
            model_name='dbchanges',
            name='update_check',
            field=models.BigIntegerField(default=1458423253.0219128),
        ),
        migrations.AlterField(
            model_name='load',
            name='created_date',
            field=models.BigIntegerField(default=1458423253.0239148),
        ),
        migrations.AlterField(
            model_name='node',
            name='name',
            field=models.CharField(default='Untitled Node', max_length=100),
        ),
        migrations.AlterField(
            model_name='syncgenerator',
            name='created_date',
            field=models.BigIntegerField(default=1458423253.024916),
        ),
        migrations.AlterField(
            model_name='twowindingtransformer',
            name='created_date',
            field=models.BigIntegerField(default=1458423253.0259192),
        ),
        migrations.AlterField(
            model_name='utility',
            name='created_date',
            field=models.BigIntegerField(default=1458423253.0259192),
        ),
    ]