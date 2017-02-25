# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resturants', '0004_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_by', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=1000)),
                ('time', models.DateTimeField()),
                ('resturant', models.ForeignKey(to='resturants.Resturant')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
