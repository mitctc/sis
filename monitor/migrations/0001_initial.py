# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 10:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedule', '0005_auto_20151227_1536'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LabAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('practical', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='schedule.LabSession')),
            ],
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PracticalAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('practical', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='schedule.PracticalSession')),
            ],
        ),
        migrations.CreateModel(
            name='TheoryAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theory', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='schedule.TheorySession')),
            ],
        ),
    ]