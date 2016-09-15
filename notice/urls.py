from django.conf.urls import url, include
from notice.views import *

app_name='notice'

urlpatterns = [

   	url(r'^all_notifications/$', NotificationsView, name='all_notifications'),

	url(r'^notified/$', NoticeBooleanUpdate, name='notified'),


]
