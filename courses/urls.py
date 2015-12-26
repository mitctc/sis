from django.conf.urls import patterns, url
from courses import views
##
urlpatterns = patterns('', 
				url(r'^$', views.index, name='index'),
				
				 url(r'^add_course/', views.add_course, name='add_course'), )# NEW MAPPING!