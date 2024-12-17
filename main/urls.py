from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('schedule', views.schedule, name='schedule'),
    path('contact', views.contact, name='contact'),
    path('coaches', views.coaches, name='coaches'),
    path('events/',include('events.url') ),

]