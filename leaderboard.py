import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ca_portal.settings")
application = get_wsgi_application()


from ca.models import CAProfile, LeaderBoard
from task.models import TaskInstance

for ca in CAProfile.objects.all():
    if ca.isChoosen:
        dd = TaskInstance.objects.get(task__taskName = 'Director Contact Details', ca = ca)
        dd.status = dd.status/10
        dd.save()
        sbd = TaskInstance.objects.get(task__taskName = 'Student Body Head Details', ca = ca)
        sbd.status = sbd.status/10
        sbd.save()
        try:
            lb = LeaderBoard.objects.create(ca=ca, points=0)
            print ca
            print 'done'
        except Exception as e:
            print e, ca.user.email
