# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20160131_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='power',
            name='type',
            field=models.IntegerField(default=0),
        ),
    ]
