# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-19 03:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('people_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DurationField(verbose_name=0)),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_provider.People')),
            ],
        ),
        migrations.AddField(
            model_name='people',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_provider.Place'),
        ),
    ]