from django.contrib import admin

from task.models import *

admin.site.register(Task)
admin.site.register(TaskInstance)
admin.site.register(DirectorDetail)
admin.site.register(StudentBodyDetail)
