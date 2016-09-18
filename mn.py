import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ca_portal.settings")
application = get_wsgi_application()

from notice.models import UserNotification
from ca.models import CAProfile

mn = raw_input('Enter the mass notification:\n\n')

print '\nEntered mass notification :\n\n'+mn

flag = raw_input('\nAre you sure to send this as mass notification [y/n] :')

user_count = CAProfile.objects.all().count()

if flag == 'y':
    for i in range(0,user_count):
        ca = CAProfile.objects.all()[i]
        UserNotification.objects.create(ca=ca,message=mn)
        print 'CA ' str(i) + ' sent!'

else:
    print 'Abort\n'
