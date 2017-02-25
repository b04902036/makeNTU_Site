# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
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
            ],
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('line', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='showFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x', models.DecimalField(default=0, max_digits=10, decimal_places=6)),
                ('y', models.DecimalField(default=0, max_digits=10, decimal_places=6)),
                ('vacancy', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='line',
            name='file',
            field=models.ForeignKey(to='raw.showFile'),
        ),
        migrations.AddField(
            model_name='bike',
            name='user',
            field=models.ForeignKey(to='raw.User'),
        ),
    ]
