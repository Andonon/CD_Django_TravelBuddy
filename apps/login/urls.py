''' App URLS.py file. '''
from django.conf.urls import url
from . import views

app_name = "auth"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^mainpage$', views.mainpage, name='mainpage'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
]
