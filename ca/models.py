from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import URLValidator
# from django.core.validators import MaxValueValidator
# from TechnexUser.models import College,year_choices

year_choices = [
        (None,'Year of study'),
        (1, 'First'),
        (2, 'Second'),
        (3, 'Third'),
        (4, 'Fourth'),
        (5,'Fifth'),
    ]

class College(models.Model):
    collegeId = models.AutoField(primary_key = True)
    collegeName = models.CharField(max_length=250)
    def __unicode__(self):
        return self.collegeName


class CAProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    year = models.IntegerField(choices=year_choices,null=True,blank=True)
    mobile_number = models.BigIntegerField(null=True)
    whatsapp_number = models.BigIntegerField(null=True)
    college = models.ForeignKey(College,null = True)
    postal_address = models.TextField(null=True)
    pinCode = models.BigIntegerField(null=True)
    profile_photo = models.TextField(validators=[URLValidator()],blank=True)
    whyChooseYou = models.TextField(blank=True,null=True)
    pastExp = models.TextField(blank=True, null=True)

    regNum = models.IntegerField(null=True,blank=True)
    firstVisit = models.BooleanField(default=False)
    isChoosen = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s-%s' %(self.user.first_name, self.college)

class LeaderBoard(models.Model):
    ca = models.OneToOneField(CAProfile)
    points = models.IntegerField(null=True)
