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
        mytrips = Destination.objects.filter(planned_by=request.session['id'])
        otherstrips = Destination.objects.all().exclude(planned_by=request.session['id'])
        print "*"*50, mytrips, "*"*50
        context = {
            'mytrips': mytrips
        }
        return render(request, 'travels/index.html', context)
    else: 
        return redirect('/')

def addplan(request): 
    ''' This is the landing page to add travel plans
    '''
    if checklogin(request):
        if request.method == "POST":
            print "*"*150, request.POST, "*"*150
            plandata = {
                'destination': request.POST['destination'],
                'description': request.POST['description'],
                'traveldatefrom': request.POST['traveldatefrom'],
                'traveldateto': request.POST['traveldateto'],
                'planned_by': request.session['id']
            }
            newtravelplanvalidate = Destination.objects.newtravelplanvalidate(plandata)
            if newtravelplanvalidate['status'] is False:
                for error in newtravelplanvalidate['errors']:
                    messages.error(request, error)
                return redirect('/travels/addplan')
            return redirect('/travels')
        else: 
            return render(request, 'travels/addplan.html')
    else:
        return redirect('/')

