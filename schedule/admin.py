from django.contrib import admin
from schedule.models import TheorySession,LabSession,PracticalSession

# Add in this class to customized the Admin Interface


# Update the registeration to include this customised interface
admin.site.register(PracticalSession)
admin.site.register(LabSession)
admin.site.register(TheorySession)