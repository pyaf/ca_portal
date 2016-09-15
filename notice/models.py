from __future__ import unicode_literals

from django.db import models
from ca.models import CAProfile

class MassNotification(models.Model):
    ca = models.ManyToManyField(CAProfile)
    mass_message = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True, blank=True)
    mark_read = models.ManyToManyField(CAProfile, related_name='mark_read',blank=True)

    def __unicode__(self):
        return self.mass_message

# bom = user.massnotification_set.all().order_by('-creation_time')
#request.user.massnotification_set.all()
#


class UserNotification(models.Model):
    ca = models.ForeignKey(CAProfile)
    message = models.TextField()
    mark_read = models.BooleanField(default=False)
    creation_time = models.DateTimeField(auto_now_add=True, blank=True)

    def __unicode__(self):
        return self.message

#request.user.usernotification_set.all()
