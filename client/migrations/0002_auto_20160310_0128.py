# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-10 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='name',
            field=models.CharField(default='Untitled Node', max_length=100),
        ),
        migrations.AlterField(
            model_name='bus',
            name='a_created_date',
            field=models.BigIntegerField(default=1457598510.1617732),
        ),
        migrations.AlterField(
            model_name='connection',
            name='created_date',
            field=models.BigIntegerField(default=1457598510.1597712),
        ),
        migrations.AlterField(
            model_name='dbchanges',
            name='update_check',
            field=models.BigIntegerField(default=1457598510.1587708),
        ),
        migrations.AlterField(
            model_name='load',
            name='created_date',
            field=models.BigIntegerField(default=1457598510.160772),
        ),
        migrations.AlterField(
            model_name='syncgenerator',
            name='created_date',
            field=models.BigIntegerField(default=1457598510.1617732),
        ),
        migrations.AlterField(
            model_name='twowindingtransformer',
            name='created_date',
            field=models.BigIntegerField(default=1457598510.1637747),
        ),
        migrations.AlterField(
            model_name='utility',
            name='a_created_date',
            field=models.BigIntegerField(default=1457598510.162774),
        ),
    ]
