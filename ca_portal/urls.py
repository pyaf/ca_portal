from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('ca.urls')),

    url(r'^', include('task.urls')),

    url(r'^admin/', admin.site.urls),

    url(r'^',include('notice.urls')),
]
