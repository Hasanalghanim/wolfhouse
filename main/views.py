from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Membership, Training, Background, Coach

# Create your views here.


def home(request):
    memberships = Membership.objects.all()
    training = Training.objects.all()
    backgrounds = Background.objects.filter(deleted=False)
    return render(request, "home.html",{"memberships": memberships, "trainings":training, "backgrounds":backgrounds})



def coaches(request):
    filter_type = request.GET.get('filter', 'Head Coach')
    activeCoaches = Coach.objects.filter(deleted=False, disciple__icontains=filter_type).order_by('orderNumber')

    return render(request, "coaches.html", {'coaches' : activeCoaches, 'filter_type': filter_type})







def schedule(request):
    return render(request, "schedule.html",)



def contact(request):
    return render(request, "contact.html",)