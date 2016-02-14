from django.db import models
from django.contrib.auth.models import User
from schedule.models import TheorySession, PracticalSession, LabSession
from course.models import Activity
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class TheoryAttendance (models.Model):
	theory = models.OneToOneField(TheorySession)
	is_present = models.BooleanField(default=False)

class PracticalAttendance (models.Model):
	practical = models.OneToOneField(PracticalSession)
	is_present = models.BooleanField(default=False)

class LabAttendance  (models.Model):
	practical = models.OneToOneField(LabSession)
	is_present = models.BooleanField(default=False)

class Performance (models.Model):

	user = models.OneToOneField(User)
	activity = models.ForeignKey(Activity)
	marks = models.IntegerField(default=1,
    validators=[MaxValueValidator(100), MinValueValidator(0)]     )
