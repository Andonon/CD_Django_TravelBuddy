# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models

# Create your models here.
class DestinationManager(models.Manager):
    def newtravelplanvalidate(self, postdata):
        print "*"*150, postdata, "*"*150
        results = {'status':True, 'errors':[]}
        if not postdata['destination'] or len(postdata['destination']) < 0:
            results['errors'].append("Destination is missing.")
            results['status'] = False
        if not postdata['description'] or len(postdata['description']) < 0:
            results['errors'].append("Description is missing.")
            results['status'] = False
        if not postdata['traveldatefrom']:
            results['errors'].append("Travel From Date is missing.")
            results['status'] = False
        if not postdata['traveldateto']:
            results['errors'].append("Travel To Date is missing.")
            results['status'] = False
        ####### I DOn't know how to get date comparisons working ###
        # if postdata['traveldateto']:
        #     results['errors'].append("Travel From Date must be in the future.")
        #     results['status'] = False
        # if postdata['traveldatefrom']: 
        #     results['errors'].append("Travel To Date must be after Travel From date.")
        #     results['status'] = False
        # if results['status'] is False:
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
