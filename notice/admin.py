from django.contrib import admin

from notice.models import *

class MassNotificationAdmin(admin.ModelAdmin):
    list_display = ['mass_message']

class UserNotificationAdmin(admin.ModelAdmin):

    def name(obj):
        return "%s" % (obj.ca.user.first_name)
    def College(obj):
        return "%s" % (obj.ca.college)


    list_display = [name,College,'message','mark_read']
admin.site.register(MassNotification, MassNotificationAdmin)
admin.site.register(UserNotification, UserNotificationAdmin)
