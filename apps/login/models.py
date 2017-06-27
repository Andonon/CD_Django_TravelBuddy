# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def registervalidate(self, postdata):
        results = {'status':True, 'errors':[], 'user':None}
        if not postdata['name'] or len(postdata['name']) < 3:
            results['errors'].append("Name must be at least 3 characters")
            results['status'] = False
        if not postdata['username'] or len(postdata['username']) < 3:
            results['errors'].append("Username must be at least 3 characters")
            results['status'] = False
        if not postdata['userpassword'] or len(postdata['userpassword']) < 8:
            results['errors'].append("Password must be at least 8 characters")
            results['status'] = False
        if postdata['cpassword'] != postdata['userpassword']:
            results['errors'].append("Passwords do not match")
            results['status'] = False
        if results['status'] is False:
            return results
        user = User.objects.filter(username=postdata['username'])
        if user:
            results['status'] = False
            results['errors'].append("Registration Failure, have you tried to login?")
        if results['status']:
            userpassword = bcrypt.hashpw(postdata['userpassword'].encode(), bcrypt.gensalt())
            user = User.objects.create(
                name=postdata['name'],
                username=postdata['username'],
                userpassword=userpassword)
            results['user'] = user
        return results

    def loginvalidate(self, postdata):
        results = {'status':True, 'errors':[], 'user':None}
        user = User.objects.filter(username=postdata['username'])
        try:                #need this try loop if the db is empty.
            user[0]
        except IndexError:
            results['status'] = False
            results['errors'].append("Account or password failure.")
            return results
        if user[0]:
            if user[0].userpassword != bcrypt.hashpw(postdata['userpassword'].encode(),
                                                     user[0].userpassword.encode()):
                results['status'] = False
                results['errors'].append("Account or password failure.")
            else:
                results['user'] = user[0].id
        else:
            results['status'] = False
        return results

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    userpassword = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name + "," + self.username
    objects = UserManager()
    #UsersDestinations