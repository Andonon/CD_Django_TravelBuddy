# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from ..login import views
from models import Destination

# Create your views here.
def checklogin(request):
    try:
        request.session['id']
    except KeyError:
        request.session.flush()
        messages.error(request, 'Oh Snap! There is no session cookie detected, please login.')
        return False
    return True

def index(request):
    ''' Main landing page for the Travels app
    '''
    if checklogin(request):
        mytrips = Destination.objects.all()
        print mytrips
        context = {
            mytrips: mytrips
        }
        return render(request, 'travels/index.html', context)
    else: 
        return redirect('/')

def addplan(request): 
    ''' This is the landing page to add travel plans
    '''
    if checklogin(request):
        return render(request, 'travels/addplan.html')
    else:
        return redirect('/')