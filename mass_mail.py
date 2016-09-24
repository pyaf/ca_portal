import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ca_portal.settings")
application = get_wsgi_application()
from django.contrib.auth.models import User
import requests

def send_email(recipient, subject, body):

    return requests.post(
        "https://api.mailgun.net/v3/mg.technex.in/messages",
        auth=("api", "key-cf7f06e72c36031b0097128c90ee896a"),
        data={"from": "No-reply <mailgun@mg.technex.in>",
              "to": recipient,
              "subject": subject,
              "text": body})


all_users = User.objects.all()
subject = raw_input('Subject : ')
body = raw_input('Body : ')

for user in all_users:
    try:
        send_email(recipient, subject, body)
        print 'sent %s' %user.email
    except Exception as e:
        print e
