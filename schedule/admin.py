from django.contrib import admin
from schedule.models import TheorySession,LabSession,PracticalSession,CourseGroup

# Add in this class to customized the Admin Interface
@admin.register(TheorySession)
class TheorySessionAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(LabSession)
class LabSessionAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(PracticalSession)
class PracticalSessionAdmin(admin.ModelAdmin):
    list_display = ('name', )
	
	
@admin.register(CourseGroup)
class CourseGroupAdmin(admin.ModelAdmin):
	list_display = ('name', )
# # Update the registeration to include this customised interface
# admin.site.register(PracticalSession,TheorySessionAdmin)
# admin.site.register(LabSession,LabSessionAdmin)
# admin.site.register(TheorySession,PracticalSession)
