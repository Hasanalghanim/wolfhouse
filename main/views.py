from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse,HttpResponseForbidden
from .models import Membership, Training, Background, Coach
from events.models import Event
from django.utils import timezone
from django.contrib.auth import authenticate, login,logout




# Create your views here.


def home(request):
    nowDate = timezone.now()
    memberships = Membership.objects.all()
    training = Training.objects.all()
    backgrounds = Background.objects.filter(deleted=False)
    events = Event.objects.filter(deleted=False, date__gte=nowDate)
    return render(request, "home.html",{"memberships": memberships, "trainings":training, "backgrounds":backgrounds, "events":events})



def coaches(request):
    filter_type = request.GET.get('filter', 'Head Coach')
    activeCoaches = Coach.objects.filter(deleted=False, disciple__icontains=filter_type).order_by('orderNumber')

    return render(request, "coaches.html", {'coaches' : activeCoaches, 'filter_type': filter_type})







def schedule(request):
    return render(request, "schedule.html",)



def contact(request):
    return render(request, "contact.html",)


def about(request):
    return render(request, 'about.html')



def login_view(request):
    if request.method == "POST":
        if request.POST.get("bot_field"):
            return HttpResponseForbidden("Form Error. Bot Attempted this form.")

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            nowDate = timezone.now()
            memberships = Membership.objects.all()
            training = Training.objects.all()
            backgrounds = Background.objects.filter(deleted=False)
            events = Event.objects.filter(deleted=False, date__gte=nowDate)
            return render(
                request,
                "home.html",
                {
                    "memberships": memberships,
                    "trainings": training,
                    "backgrounds": backgrounds,
                    "events": events,
                    "login_modal_open": True,
                    "login_error": "Invalid username or password",
                },
            )
    else:
        return redirect("home")


def logout_view(request):
    logout(request)
    return redirect('home')

