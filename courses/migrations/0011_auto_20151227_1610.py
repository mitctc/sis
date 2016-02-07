# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20151227_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='fees',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=16),
        ),
        migrations.AlterField(
            model_name='course',
            name='fees',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=16),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='fees',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=16),
        ),
        migrations.AlterField(
            model_name='topic',
            name='fees',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=16),
        ),
    ]
