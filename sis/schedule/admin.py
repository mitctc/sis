from django.contrib import admin
from schedule.models import TheorySession,LabSession,PracticalSession


# Add in this class to customized the Admin Interface
class TheorySessionAdmin(admin.ModelAdmin):
	#prepopulated_fields = {'slug':('name',)}
	list_display = ('name', )
	
class LabSessionAdmin(admin.ModelAdmin):
	#prepopulated_fields = {'slug':('name',)}
	list_display = ('name', )

class PracticalSessionAdmin(admin.ModelAdmin):
	#prepopulated_fields = {'slug':('name',)}
	list_display = ('name', )

admin.site.register(TheorySession,TheorySessionAdmin)
admin.site.register(LabSession,LabSessionAdmin)
admin.site.register(PracticalSession,PracticalSessionAdmin)
