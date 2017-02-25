# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('raw', '0005_bike_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 26, 6, 44, 9, 863000), blank=True),
        ),
    ]
