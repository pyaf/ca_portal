from __future__ import unicode_literals

from django.db import models

from ca.models import CAProfile

class Task(models.Model):
    taskId = models.AutoField(primary_key = True)
    taskName = models.CharField(max_length = 50)
    taskDescription = models.TextField()
    deadLine = models.DateTimeField()
    def __unicode__(self):
        return self.taskName

class TaskInstance(models.Model):
    task = models.ForeignKey(Task)
    ca = models.ForeignKey(CAProfile)
    status = models.SmallIntegerField(default = 0) #Added this field to show partial completion(0-10) of work
    def __unicode__(self):
        return '%s'%self.status

class DirectorDetail(models.Model):
    directorDetail = models.TextField() #dd = BooleanField for directorDetail
    ca = models.OneToOneField(CAProfile)

    def __unicode__(self):
        return "%s" %self.ca

class StudentBodyDetail(models.Model):
    studentBodyDetail = models.TextField()
    ca = models.OneToOneField(CAProfile)

    def __unicode__(self):
        return "%s" %self.ca


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
