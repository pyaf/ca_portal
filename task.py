import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ca_portal.settings")
application = get_wsgi_application()

from ca.models import CAProfile
from task.models import Task, TaskInstance
from django.utils import timezone


Task.objects.create(taskName='Director Contact Details',
                    taskDescription='Provide us the details of Director of your college.',
                    deadLine=timezone.now())

Task.objects.create(taskName='Student Body Head Details',
                    taskDescription='Provide us the Details of Student Body Head of your college.',
                    deadLine=timezone.now())

Task.objects.create(taskName='facebook connect',
                    taskDescription='Give us the permission to automatically like Technex Facebook Page',
                    deadLine=timezone.now())

tasks = Task.objects.all()
print tasks
CAs = CAProfile.objects.all()

for ca in CAs:
    print ca
    for task in tasks:
        taskInstance = TaskInstance(task = task, ca = ca)
        taskInstance.save()
        print ca, taskInstance
    print '\n'
