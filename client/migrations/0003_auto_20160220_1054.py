# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20160217_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='power',
            name='load',
            field=models.FloatField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='power',
            name='created_date',
            field=models.BigIntegerField(default=1455990879.404975),
        ),
    ]
