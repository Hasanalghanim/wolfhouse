from django.shortcuts import render, HttpResponse
from .models import Membership, Training

# Create your views here.


def home (request):
    memberships = Membership.objects.all()
    training = Training.objects.all()
    return render(request, "home.html",{"memberships": memberships, "trainings":training})



def schedule (request):
    return render(request, "schedule.html",)