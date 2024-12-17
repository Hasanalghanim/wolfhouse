from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.eventDetail, name='all events'),
    path('fight-card/<str:event_id>',views.eventDetail, name='eventDetail'),
    path('register-participant',views.register_participant, name='register_participant'),


]