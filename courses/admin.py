from django.contrib import admin
from courses.models import Course , Topic,Lesson,Activity,CourseModule,Teachers_Diary


# Add in this class to customized the Admin Interface
class CourseAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}
	list_display = ('name', )
	
class CourseModuleAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}
	list_display = ('name', )
	
class TopicAdmin(admin.ModelAdmin):
	list_display = ('name', )
	
class Teachers_DiaryAdmin(admin.ModelAdmin):
	list_display = ("activity",)
	
class LessonAdmin(admin.ModelAdmin):
	list_display = ('name', )
	
class ActivityAdmin(admin.ModelAdmin):
	list_display = ('name', )
# Update the registeration to include this customised interface

admin.site.register(Course, CourseAdmin)
admin.site.register(CourseModule, CourseModuleAdmin)
admin.site.register(Topic,TopicAdmin)
admin.site.register(Lesson,LessonAdmin)
admin.site.register(Activity,ActivityAdmin)
admin.site.register(Teachers_Diary,Teachers_DiaryAdmin)
