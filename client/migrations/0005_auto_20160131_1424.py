# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20160131_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='power',
            name='created_date',
            field=models.BigIntegerField(default=1454275493.7802408),
        ),
    ]
