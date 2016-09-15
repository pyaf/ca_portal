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
