# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-19 05:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_provider', '0003_placepeopletime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placepeopletime',
            name='people',
        ),
        migrations.RemoveField(
            model_name='placepeopletime',
            name='place',
        ),
        migrations.RemoveField(
            model_name='placepeopletime',
            name='time',
        ),
        migrations.DeleteModel(
            name='PlacePeopleTime',
        ),
    ]
