# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class DestinationManager(models.Manager):
    pass

class Destination(models.Model):
    ''' This is the main desctination module, aka Trips, and contains the Plan, aka description
    '''
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    traveldatefrom = models.DateField()
    traveldateto = models.DateField()
    planned_by = models.ForeignKey('login.User', related_name="UsersDestinations")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    participants = models.ManyToManyField('login.User', related_name="allparticipants")
    objects = DestinationManager()
