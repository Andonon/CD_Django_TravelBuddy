# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.
class DestinationManager(models.Manager):
    def newtravelplanvalidate(self, postdata):
        results = {'status':True, 'errors':[]}
        if not postdata['destination'] or len(postdata['destination']) < 0:
            results['errors'].append("Destination is missing.")
            results['status'] = False
        if not postdata['description'] or len(postdata['description']) < 0:
            results['errors'].append("Description is missing.")
            results['status'] = False
        if not postdata['traveldatefrom']:
            results['errors'].append("Travel Departure Date is missing.")
            results['status'] = False
        else:
            if datetime.strptime(postdata['traveldatefrom'], "%Y-%m-%d") < datetime.today():
                results['errors'].append("Travel Departure Date must be in the future.")
                results['status'] = False
        if not postdata['traveldateto']:
            results['errors'].append("Travel Return Date is missing.")
            results['status'] = False
        else:
            if datetime.strptime(postdata['traveldateto'], "%Y-%m-%d") \
            < datetime.strptime(postdata['traveldatefrom'], "%Y-%m-%d"):
                results['errors'].append("Travel Return Date must be after departure date.")
                results['status'] = False
        if results['status'] is False:
            return results
        else:
            createtrip = Destination.objects.create(
                name=postdata['destination'],
                description=postdata['description'],
                traveldatefrom=postdata['traveldatefrom'],
                traveldateto=postdata['traveldateto'],
                planned_by_id=postdata['planned_by'])
            return results


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
