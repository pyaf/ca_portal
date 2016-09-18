import requests
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ca_portal.settings")
application = get_wsgi_application()

from ca.models import CAProfile

def SheetUpdate(caprofile):
    dic = {
    'name' : caprofile.user.first_name,
    'email' : caprofile.user.email,
    'college' : caprofile.college,
    'year' : caprofile.year,
    'mobileNumber': caprofile.mobile_number,
    'whatsappNumber': caprofile.whatsapp_number,
    'postalAddress' : caprofile.postal_address,
    'pincode': caprofile.pinCode,
    'whyChooseYou': caprofile.whyChooseYou,
    'pastExp':caprofile.pastExp,
    }

    url = 'https://script.google.com/macros/s/AKfycbzEw71pbzcam4W2Jh9-bExZU7Ocv_fBULgmZBf7rMSxwdrHYY0/exec'
    requests.post(url,data=dic)

count = CAProfile.objects.all().count()
for i in range(0,count):
    caprofile = CAProfile.objects.all()[i]
    SheetUpdate(caprofile)
    print caprofile
