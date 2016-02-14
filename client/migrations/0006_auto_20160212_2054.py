# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_auto_20160131_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='power',
            name='created_date',
            field=models.BigIntegerField(default=1455335696.1310437),
        ),
    ]
