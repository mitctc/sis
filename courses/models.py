from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Course(models.Model):
	code = models.CharField(max_length=5,unique=True)
	name = models.CharField(max_length=128)
	views = models.IntegerField(default=0)
	
	def __unicode(self):
		return self.name 
		
class Topic(models.Model):
	course = models.ForeignKey(Course)
	code = models.CharField(max_length=5,unique=True)
	name = models.CharField(max_length=128)
	
	def __unicode(self):
		return self.name 