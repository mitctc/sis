from django.db import models
from django.contrib.auth.models import User
from schedule.models import TheorySession, PracticalSession, LabSession
from courses.models import Activity

# Create your models here.
class TheoryAttendance (models.Model):
	theory = models.OneToOneField(TheorySession)

class PracticalAttendance (models.Model):
	practical = models.OneToOneField(PracticalSession)

class LabAttendance  (models.Model):
	practical = models.OneToOneField(LabSession)

class Performance (models.Model):

	user = models.OneToOneField(User)
	models.ForeignKey(Activity)