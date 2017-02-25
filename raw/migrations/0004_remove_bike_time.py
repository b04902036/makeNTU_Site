# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raw', '0003_bike'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bike',
            name='time',
        ),
    ]
