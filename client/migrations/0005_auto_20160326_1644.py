# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-26 23:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20160326_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bus',
            name='nominal_voltage',
        ),
        migrations.RemoveField(
            model_name='load',
            name='nominal_voltage',
        ),
        migrations.RemoveField(
            model_name='syncgenerator',
            name='nominal_voltage',
        ),
        migrations.RemoveField(
            model_name='utility',
            name='nominal_voltage',
        ),
        migrations.AddField(
            model_name='node',
            name='nominal_voltage',
            field=models.FloatField(default=0.0, max_length=100),
        ),
        migrations.AlterField(
            model_name='connection',
            name='created_date',
            field=models.BigIntegerField(default=1459035869.5247054),
        ),
        migrations.AlterField(
            model_name='dbchanges',
            name='update_check',
            field=models.BigIntegerField(default=1459035869.5237045),
        ),
        migrations.AlterField(
            model_name='node',
            name='created_date',
            field=models.BigIntegerField(default=1459035869.5247054),
        ),
    ]