from django.shortcuts import render, HttpResponse
from .models import Membership, Training, Background

# Create your views here.


def home (request):
    memberships = Membership.objects.all()
    training = Training.objects.all()
    backgrounds = Background.objects.filter(deleted=False)
    return render(request, "home.html",{"memberships": memberships, "trainings":training, "backgrounds":backgrounds})



def schedule (request):
    return render(request, "schedule.html",)



def contact (request):
    return render(request, "contact.html",)