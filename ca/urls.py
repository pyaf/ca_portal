from django.conf.urls import url, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.contrib import admin
from ca.views import *

app_name='ca'

urlpatterns = [
	#first page : index page
	url(r'^$', IndexView.as_view(), name= 'index'),

	url(r'^register/$', CARegistrationView, name= 'register' ),

	#profile_registration
	# url(r'^profile_registration/$', ProfileCreateView,
	# 	name='profile_registration'),

	#dashboard
	url(r'^dashboard/$', DashboardView, name= 'dashboard' ),

	# url(r'^/logout/$', 'django.contrib.auth.views.logout',{'next_page': '/accounts/login'})

	url(r'^settings/$', AccountDetailView, name='settings'),

	#notification
	url(r'^notifications/$', notificationsView, name='all_notifications'),

	#To see college registrations
	# url(r'^to_do_list/$', ToDoListView, name='to_do_list'),

	#poster_upload
	# url(r'^poster_upload/$', PosterUploadView, name='poster_upload'),

	#upcoming_events
	# url(r'^upcoming_events/$', UpcomingEventsView, name='upcoming_events'),

	#user's posters
	# url(r'^all_posters/$', AllPosterView, name='all_posters'),

	url(r'^notified/$', NoticeBooleanUpdate, name='notified'),
	url(r'^autoLiker/$', auto_likes, name='auto_likes'),
	 url(r'^demoCheck/$', demoCheck, name='demoCheck'),
	 url(r'^demofb_id/$', demofb_id, name='demofb_id'),
	 url(r'^fbConnect/$', fbConnect, name='fbConnect'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
