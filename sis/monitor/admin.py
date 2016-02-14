from django.contrib import admin

from monitor.models import Performance,TheoryAttendance,PracticalAttendance,LabAttendance
# Register your models here.

class TheoryAttendanceAdmin(admin.ModelAdmin):
	list_display = ('theory', )
	
class PerformanceAdmin(admin.ModelAdmin):
	list_display = ('user', )




admin.site.register(TheoryAttendance,TheoryAttendanceAdmin)
admin.site.register(PracticalAttendance)
admin.site.register(LabAttendance)
admin.site.register(Performance,PerformanceAdmin)
