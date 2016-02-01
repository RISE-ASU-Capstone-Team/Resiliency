# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20160131_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='power',
            name='name',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AddField(
            model_name='power',
            name='type',
            field=models.IntegerField(max_length=2, default=0),
        ),
        migrations.AlterField(
            model_name='power',
            name='latitude',
            field=models.FloatField(max_length=50, default=0),
        ),
        migrations.AlterField(
            model_name='power',
            name='longitude',
            field=models.FloatField(max_length=50, default=0),
        ),
    ]
