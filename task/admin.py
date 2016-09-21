from django.contrib import admin

from task.models import *



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

admin.site.register(FbConnect)
admin.site.register(ForgetPass)