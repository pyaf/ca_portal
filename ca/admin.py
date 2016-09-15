from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
# from django.contrib.admin.options import ModelAdmin
from ca.models import *
#Define an inline admin descriptor for UserProfile model

# class UserStatusInline(admin.StackedInline):
#     model = UserStatus
#     can_delete = False


class UserAdmin(UserAdmin):

    def name(obj):
        return "%s" % (obj.first_name)


    def college(obj):
        try:
            return "%s" % obj.caprofile.college
        except:
            return "No college"

    def mobile_number(obj):
        try:
            return "%s" % obj.caprofile.mobile_number
        except:
            return "None"

    # def CA(obj):
    #     try:
    #         return "%s" %obj.userstatus.is_ca
    #     except:
    #         return "None"
    #
    # def TechUser(obj):
    #     try:
    #         return "%s" %obj.userstatus.is_techuser
    #     except:
    #         return "None"

    name.short_description = 'Name'

    # inlines = (UserStatusInline, )
    list_display = ('email',name, college, mobile_number)



#obj is the model you are referencing.

#Re-register UserAdmin
admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(CAProfile)
admin.site.register(User,UserAdmin)

# admin.site.register(TechnexUser,TechnexUserAdmin)
