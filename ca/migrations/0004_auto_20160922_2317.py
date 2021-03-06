# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-22 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ca', '0003_caprofile_pincode'),
    ]

    operations = [
        migrations.AddField(
            model_name='caprofile',
            name='firstVisit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='caprofile',
            name='regNum',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='caprofile',
            name='year',
            field=models.IntegerField(blank=True, choices=[(None, b'Year of study'), (1, b'First'), (2, b'Second'), (3, b'Third'), (4, b'Fourth'), (5, b'Fifth')], null=True),
        ),
    ]
