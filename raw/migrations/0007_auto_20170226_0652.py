# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('raw', '0006_auto_20170226_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='diffTime',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bike',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 26, 6, 52, 9, 125000), blank=True),
        ),
    ]
