#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    #path('page/',views.basee, name='page'),
     path('', views.index, {'pagename': ''}, name='home'),
     path('contact', views.contact, name='contact'),
     path('<str:pagename>', views.index, name='index'),
]