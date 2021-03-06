# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-27 11:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=20)),
                ('registration', models.CharField(max_length=10)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AircraftMajorAssembly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assembly_name', models.CharField(max_length=100)),
                ('part_number', models.CharField(max_length=20)),
                ('serial_number', models.CharField(max_length=20)),
                ('delta_hours', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='AircraftType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type_certificate', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('contact_person', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('billing_address', models.TextField(blank=True, null=True)),
                ('shipping_address', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='aircraft',
            name='aircraft_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.AircraftType'),
        ),
        migrations.AddField(
            model_name='aircraft',
            name='major_assemblies',
            field=models.ManyToManyField(to='database.AircraftMajorAssembly'),
        ),
    ]
