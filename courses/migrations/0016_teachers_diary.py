# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_activity_activity_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers_Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_completed', models.BooleanField()),
                ('activity', models.ForeignKey(to='courses.Activity')),
            ],
        ),
    ]
