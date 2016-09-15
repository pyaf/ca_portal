from django.db import models
from allauth import app_settings as allauth_app_settings
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import URLValidator
# from django.core.validators import MaxValueValidator
from TechnexUser.models import College,year_choices


class CAProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    year = models.IntegerField(choices=year_choices,null=True,blank=True)
    mobile_number = models.BigIntegerField(null=True)
    whatsapp_number = models.BigIntegerField(null=True)
    college = models.ForeignKey(College,null = True)
    college_address = models.TextField(null=True)
    postal_address = models.TextField(null=True)
    profile_photo = models.TextField(validators=[URLValidator()],blank=True)
    whyChooseYou = models.TextField(blank=True,null=True)
    pastExp = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return '%s-%s' %(self.user.first_name, self.college)


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

#primary_key=True implies null=False and unique=True.
#Only one primary key is allowed on an object.
def get_user_image_folder(instance, filename):
    return "CAs/%s-%s-%s/%s" %(instance.user.first_name,instance.user.last_name,instance.user.caprofile.college, filename)
#You don't have to use request in Models, you use instance instead.

class Poster(models.Model):
    ca = models.ForeignKey(CAProfile)
    poster = models.ImageField(upload_to = get_user_image_folder)

    def __unicode__(self):
        return '%s' % self.poster

# @receiver(post_save, sender=User)
# def create_profile(sender,created, instance, **kwargs):
#     if created:
#         user_profile = UserProfile(user = instance)
#         user_profile.save()

    # #where to redirect after successful userprofile registration
    # def get_absolute_url(self):
    #     return reverse('dashboard',kwargs={'pk':self.pk})
    # or
    # def get_absolute_url(self):
    #     return u'/some_url/%d' % self.id

class FbConnect(models.Model):
    ca = models.ForeignKey(CAProfile)
    accessToken = models.CharField(max_length = 150,null = True,blank = True)
    uid = models.CharField(max_length = 150,null = True, blank = True)
    def __unicode__(self):
        return self.uid
