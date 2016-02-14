# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_auto_20160213_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='power',
            name='created_date',
            field=models.BigIntegerField(default=1455420590.6351254),
        ),
    ]
