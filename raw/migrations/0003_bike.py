# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raw', '0002_auto_20170226_0638'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('myId', models.CharField(max_length=100)),
                ('x', models.DecimalField(default=0, max_digits=10, decimal_places=6)),
                ('y', models.DecimalField(default=0, max_digits=10, decimal_places=6)),
                ('status', models.BigIntegerField(default=0)),
                ('time', models.DateTimeField(auto_now=True)),
                ('diffTime', models.DecimalField(default=0, max_digits=10, decimal_places=3)),
                ('user', models.ForeignKey(to='raw.User')),
            ],
        ),
    ]
