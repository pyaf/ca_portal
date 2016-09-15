import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ca_portal.settings")
application = get_wsgi_application()
# import django
# django.setup()
import csv
from ca.models import College

with open('b.csv','rb') as f:
    data = csv.reader(f)
    for row in data:
        College.objects.create(collegeName=row[1])
        print row[1]
