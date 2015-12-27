from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models
from courses.models import CourseGroup

class TheorySession(models.Model):
	name = models.CharField(max_length=120)
	course_group = models.ForeignKey(CourseGroup)
	

class LabSession(models.Model):
	
	course_group = models.ForeignKey(CourseGroup)

class PracticalSession(models.Model):
	
	user = models.ForeignKey(User)
	course_group = models.ForeignKey(CourseGroup)
	
