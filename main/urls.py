from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('schedule', views.schedule, name='schedule'),
    path('contact', views.contact, name='contact'),
    path('coaches', views.coaches, name='coaches'),
    path('about', views.about, name='about'),
    path('events/',include('events.url') ),
    path('login', views.login_view, name='login_view'),
    path('logout', views.logout_view, name='logout_view'),

]