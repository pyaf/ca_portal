from django.conf.urls import url, include
from task.views import *

app_name='task'

urlpatterns = [
	
	url(r'^submitDirector/$', submitDirectorDetail,name='submitDirector'),
	url(r'^submitStudentBody/$',submitStudentBodyDetail,name='submitStudentBody'),
	# url(r'^dd/$', directorDetailView, name='dd'),
	# url(r'^sbd/$', studentBodyView, name='sbd'),


]
