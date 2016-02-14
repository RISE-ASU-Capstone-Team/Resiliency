# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='power',
            name='author',
        ),
        migrations.RemoveField(
            model_name='power',
            name='published_date',
        ),
        migrations.RemoveField(
            model_name='power',
            name='text',
        ),
        migrations.RemoveField(
            model_name='power',
            name='title',
        ),
        migrations.AddField(
            model_name='power',
            name='latitude',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='power',
            name='longitude',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
