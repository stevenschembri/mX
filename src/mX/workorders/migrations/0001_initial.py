# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-27 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aircraft', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=20)),
                ('station', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('customer', models.CharField(max_length=100)),
            ],
        ),
    ]
