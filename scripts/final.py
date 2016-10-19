import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ca_portal.settings")
application = get_wsgi_application()

from django.contrib.auth.models import User

import csv
with open('finalcasheet.csv','rb') as f:
    data = csv.reader(f)
    for row in data:
        print row[1]
        try:
            user = User.objects.get(username=row[1])
            user.caprofile.isChoosen = True
            user.caprofile.save()
        except Exception as e:
            print e
