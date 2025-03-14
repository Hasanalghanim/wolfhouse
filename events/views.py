
from django.shortcuts import render


from .forms import ParticipantForm
from .models import Event,  Participant

#TODO

# list of registered people 
# More info to add to event



# Create your views here.
def eventDetail(request,event_id):
    event = Event.objects.filter(id=event_id)
    participants = Participant.objects.filter(event=event_id, deleted=False).order_by("weight", "first_name")


    if request.method == "POST":
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()  # Save participant data
            return render(request, "confirmRegistration.html", {'success': True, 'event':event})
        else:
            print(form.errors)
            return render(request, "eventDetail.html", {'form': form, 'errors': form.errors,'event':event})
    
    return render(request, "eventDetail.html", {'event':event, 'participants':participants})


def register_participant(request):
    if request.method == "POST":
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()  # Save participant data
            return render(request, "eventDetail.html", {'success': True})
        else:
            return render(request, "eventDetail.html", {'form': form, 'errors': form.errors})
    return render(request, "eventDetail.html")