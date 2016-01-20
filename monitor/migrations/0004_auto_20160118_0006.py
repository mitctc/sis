# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0003_performance_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='labattendance',
            name='is_present',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='practicalattendance',
            name='is_present',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='theoryattendance',
            name='is_present',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='performance',
            name='marks',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]
