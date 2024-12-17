from django import forms
from .models import Participant

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['first_name', 'last_name', 'gender', 'date_of_birth', 'school_name', 'email', 'years_of_training', 'event']