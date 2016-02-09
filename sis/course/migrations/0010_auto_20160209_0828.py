# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-09 08:28
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0009_teachers_diary_coursegroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 2, 9, 8, 28, 44, 849748, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 2, 9, 8, 28, 51, 226440, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
