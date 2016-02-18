# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Power',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100, default='')),
                ('type', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('latitude', models.FloatField(max_length=50, default=0)),
                ('longitude', models.FloatField(max_length=50, default=0)),
                ('created_date', models.BigIntegerField(default=1455762035.873088)),
            ],
        ),
    ]
