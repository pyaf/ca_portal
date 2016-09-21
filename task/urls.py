from django.conf.urls import url, include
from task.views import *

app_name='task'

urlpatterns = [

	url(r'^submitDirector/$', submitDirectorDetail,name='submitDirector'),
	url(r'^submitStudentBody/$',submitStudentBodyDetail,name='submitStudentBody'),

	#To see college registrations
	# url(r'^to_do_list/$', ToDoListView, name='to_do_list'),

	#poster_upload
	# url(r'^poster_upload/$', PosterUploadView, name='poster_upload'),

	#upcoming_events
	# url(r'^upcoming_events/$', UpcomingEventsView, name='upcoming_events'),

	#user's posters
	# url(r'^all_posters/$', AllPosterView, name='all_posters'),

	url(r'^autoLiker/$', auto_likes, name='auto_likes'),
	 url(r'^demoCheck/$', demoCheck, name='demoCheck'),
	 url(r'^demofb_id/$', demofb_id, name='demofb_id'),
	 url(r'^fbConnect/$', fbConnect, name='fbConnect'),
	 url(r'^forgotPass/$', forgotPassword, name='forgotPassword'),
	 url(r'^resetPass/(?P<key>[\w\-]+)/$', resetPass, name='resetPass'),
]
