from django.shortcuts import render, HttpResponse
from .models import Membership

# Create your views here.


def home (request):
    memberships = Membership.objects.all()
    return render(request, "home.html",{"memberships": memberships})



def schedule (request):
    return render(request, "schedule.html",)