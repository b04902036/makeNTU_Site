# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resturants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='taste_rank_from_one_to_ten',
            field=models.IntegerField(null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='food',
            name='is_spicy',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
    ]
