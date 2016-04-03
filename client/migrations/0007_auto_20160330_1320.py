# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-30 20:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_auto_20160330_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pipe',
            fields=[
                ('connection_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='client.Connection')),
                ('diameter', models.FloatField(default=0.0, max_length=100)),
                ('flow', models.FloatField(default=0.0, max_length=100)),
                ('velocity', models.FloatField(default=0.0, max_length=100)),
                ('quality', models.FloatField(default=0.0, max_length=100)),
            ],
            bases=('client.connection',),
        ),
        migrations.AlterField(
            model_name='connection',
            name='created_date',
            field=models.BigIntegerField(default=1459369240.303483),
        ),
        migrations.AlterField(
            model_name='dbchanges',
            name='update_check',
            field=models.BigIntegerField(default=1459369240.301709),
        ),
        migrations.AlterField(
            model_name='node',
            name='created_date',
            field=models.BigIntegerField(default=1459369240.302649),
        ),
    ]
