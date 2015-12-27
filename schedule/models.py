from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models
from courses.models import CourseGroup,Activity 
from datetime import datetime 

# Theory Session table create 
# have relationship between course groups table and 
class TheorySession(models.Model):
	name = models.CharField(max_length=120)
	course_group = models.ForeignKey(CourseGroup)
	start_time = models.DateTimeField(default=datetime.now, blank=True)
	end_time = models.DateTimeField(default=datetime.now, blank=True)
	activity = models.ForeignKey(Activity)

class LabSession(models.Model):
	
	course_group = models.ForeignKey(CourseGroup)
	start_time = models.DateTimeField(default=datetime.now, blank=True)
	end_time = models.DateTimeField(default=datetime.now, blank=True)
	activity = models.ForeignKey(Activity)

class PracticalSession(models.Model):
	
	user = models.ForeignKey(User)
	start_time = models.DateTimeField(default=datetime.now, blank=True)
	end_time = models.DateTimeField(default=datetime.now, blank=True)
	activity = models.ForeignKey(Activity)
	

