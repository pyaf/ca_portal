from django.conf.urls import url, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.contrib import admin
from ca.views import *

app_name='ca'

urlpatterns = [
	#first page : index page
	url(r'^$', IndexView.as_view(), name= 'login' ),

	url(r'^login', LoginView, name= 'login' ),

	url(r'^register/$', CARegistrationView, name= 'register' ),

	# url(r'^fblogin/$', FbLogin, name= 'fblogin' ),

	url(r'^confirmEmail/(?P<confirmationKey>[\w\-]+)/$', confirmEmail, name='confirmEmail'),
	#dashboard
	url(r'^dashboard/$', DashboardView, name= 'dashboard' ),
	#
	url(r'^logout/$', LogoutView, name='name'),
	#
	url(r'^settings/$', AccountDetailView, name='settings'),
	#
	url(r'^passwordChange/$', PasswordChangeView, name='passwordChange'),


	url(r'^leaderboard/$', LeaderboardView, name='leaderboard'),

	url(r'^8727612845746360924/$', ApiReferralView)

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
