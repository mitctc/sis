# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='performance',
            name='marks',
            field=models.IntegerField(default=0),
        ),
    ]