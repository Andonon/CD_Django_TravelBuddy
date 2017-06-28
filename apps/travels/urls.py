"""travelbuddy travels app URL Configuration
"""
from django.conf.urls import url
from . import views

#app_name = travels -- set at project urls.py
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addplan$', views.addplan, name='addplan'),
    url(r'^viewplan/(?P<trip_id>\d+)$', views.viewplan, name='viewplan'),
]
