from django.urls import path
from . import views

urlpatterns = [

    path('update_webhook/', views.update_webhook, name='update_webhook'),
  
]