# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-09 08:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('fees', models.DecimalField(decimal_places=2, default=0.0, max_digits=16)),
                ('payment_type', models.CharField(choices=[('de', 'Addmision Fees'), ('pr', 'Course Fees')], max_length=15)),
            ],
        ),
    ]
