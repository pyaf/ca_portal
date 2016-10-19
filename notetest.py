import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ca_portal.settings")
application = get_wsgi_application()

from django.contrib.auth.models import User
from ca.models import CAProfile
from notice.models import UserNotification

rishabh = User.objects.get(username='rishabh.ag342@gmail.com')
ca = CAProfile.objects.get(user=rishabh)

for i in range(5):
    UserNotification.objects.create(ca=ca,message='newnew'+str(i))
    print i
print 'done!'
