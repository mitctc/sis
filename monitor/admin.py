from django.contrib import admin

from monitor.models import Performance,TheoryAttendance,PracticalAttendance,LabAttendance
# Register your models here.
admin.site.register(TheoryAttendance)
admin.site.register(PracticalAttendance)
admin.site.register(LabAttendance)
admin.site.register(Performance)