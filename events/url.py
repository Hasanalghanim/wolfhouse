from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.eventDetail, name='all events'),
    path('fight-card/<str:event_id>',views.eventDetail, name='eventDetail'),
    path('register-participant',views.register_participant, name='register_participant'),
    path('exportEventData/<int:event_id>/',views.exportEventParticipants, name='exportEventParticipants'),
    path('delete-percipient/<int:percipient>/',views.delete_participant, name='delete_participant'),
    path('<int:event_id>/match-list/', views.match_list, name='match_list'),
]