from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models
from course.models import Activity,Course,CourseGroup 
from datetime import datetime 

# Theory Session table create 
# have relationship between course groups table an



class TheorySession(models.Model):
	coursegroup = models.ForeignKey(CourseGroup)
	name = models.CharField(max_length=120)
	start_time = models.DateTimeField(default=datetime.now, blank=True)
	end_time = models.DateTimeField(default=datetime.now, blank=True)
	activity = models.ForeignKey(Activity)
	is_present= models.BooleanField()

class LabSession(models.Model):
	name = models.CharField(max_length=120)
	start_time = models.DateTimeField(default=datetime.now, blank=True)
	end_time = models.DateTimeField(default=datetime.now, blank=True)
	activity = models.ForeignKey(Activity)
	is_present= models.BooleanField()

class PracticalSession(models.Model):
	name = models.CharField(max_length=120)
	user = models.ForeignKey(User)
	start_time = models.DateTimeField(default=datetime.now, blank=True)
	end_time = models.DateTimeField(default=datetime.now, blank=True)
	activity = models.ForeignKey(Activity)
	is_present= models.BooleanField()

