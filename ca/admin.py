from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
# from django.contrib.admin.options import ModelAdmin
from ca.models import *


class UserAdmin(UserAdmin):

    def name(obj):
        return "%s" % (obj.first_name)


    def college(obj):
        return "%s" % obj.caprofile.college

    def mobile_number(obj):
        return "%s" % obj.caprofile.mobile_number


    name.short_description = 'Name'

    # inlines = (UserStatusInline, )
    list_display = ('email',name, college, mobile_number)



#obj is the model you are referencing.

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(CAProfile)
admin.site.register(User,UserAdmin)
admin.site.register(College)
