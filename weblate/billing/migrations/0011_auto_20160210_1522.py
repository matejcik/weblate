# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0010_auto_20160210_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='currency',
            field=models.IntegerField(choices=[(0, 'EUR'), (1, 'mBTC')], default=0),
        ),
    ]
