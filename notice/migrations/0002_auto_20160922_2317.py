# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-22 17:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='massnotification',
            name='ca',
        ),
        migrations.RemoveField(
            model_name='massnotification',
            name='mark_read',
        ),
        migrations.DeleteModel(
            name='MassNotification',
        ),
    ]