from django.contrib import admin

from task.models import *

class MassNotificationAdmin(admin.ModelAdmin):
    list_display = ['mass_message']

class UserNotificationAdmin(admin.ModelAdmin):

    def name(obj):
        return "%s" % (obj.ca.user.first_name)
    def College(obj):
        return "%s" % (obj.ca.college)


    list_display = [name,College,'message','mark_read']

class PosterAdmin(admin.ModelAdmin):

    def name(obj):
        return "%s" % (obj.user.first_name)

    name.short_description = 'Name'
    list_display = (name,'poster')


admin.site.register(Task)
admin.site.register(TaskInstance)
admin.site.register(DirectorDetail)
admin.site.register(StudentBodyDetail)
admin.site.register(Poster, PosterAdmin)
admin.site.register(MassNotification, MassNotificationAdmin)
admin.site.register(UserNotification, UserNotificationAdmin)
admin.site.register(FbConnect)
