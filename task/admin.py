from django.contrib import admin

from task.models import *



class PosterAdmin(admin.ModelAdmin):

    def name(obj):
        return "%s" % (obj.user.first_name)

    name.short_description = 'Name'
    list_display = (name,'poster')



class TaskInstanceAdmin(admin.ModelAdmin):

    def email(obj):
        return "%s" % (obj.ca.user.email)
    def college(obj):
        return "%s" %obj.ca.college

    list_display = (email,college,'task','status')

admin.site.register(Task)
admin.site.register(TaskInstance,TaskInstanceAdmin)
admin.site.register(DirectorDetail)
admin.site.register(StudentBodyDetail)
admin.site.register(Poster, PosterAdmin)

admin.site.register(FbConnect)
admin.site.register(Key)
