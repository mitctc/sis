# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 10:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_auto_20151227_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursegroup',
            name='course',
        ),
        migrations.RemoveField(
            model_name='coursegroup',
            name='user',
        ),
    ]