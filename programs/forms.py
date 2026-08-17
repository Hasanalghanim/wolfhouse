from django import forms
from .models import Registration


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Registration

        fields = [
            "parent_name",
            "parent_email",
            "parent_phone",
            "child_name",
            "child_dob",
            "emergency_contact",
            "emergency_phone",
            "additional_information",
            "waiver_accepted",
            "terms_accepted",
        ]

        widgets = {
            "parent_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Parent / Guardian Name"
            }),

            "parent_email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email Address"
            }),

            "parent_phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Phone Number"
            }),

            "child_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Child's Full Name"
            }),

            "child_dob": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),

            "emergency_contact": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Emergency Contact"
            }),

            "emergency_phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Emergency Phone"
            }),

            "additional_information": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Allergies, medical information, or anything else we should know..."
            }),

            "waiver_accepted": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            }),

            "terms_accepted": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            }),
        }

        labels = {
            "parent_name": "Parent / Guardian",
            "parent_email": "Email Address",
            "parent_phone": "Phone Number",
            "child_name": "Child's Full Name",
            "child_dob": "Date of Birth",
            "emergency_contact": "Emergency Contact",
            "emergency_phone": "Emergency Phone",
            "additional_information": "Additional Information",
            "waiver_accepted": "I agree to the Wolfhouse MMA waiver.",
            "terms_accepted": "I agree to the program terms and conditions.",
        }

    def __init__(self, *args, program=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.program = program

    def clean_waiver_accepted(self):
        value = self.cleaned_data["waiver_accepted"]

        if not value:
            raise forms.ValidationError(
                "You must accept the waiver."
            )

        return value

    def clean_terms_accepted(self):
        value = self.cleaned_data["terms_accepted"]

        if not value:
            raise forms.ValidationError(
                "You must accept the terms and conditions."
            )

        return value

    def clean_child_dob(self):
        dob = self.cleaned_data["child_dob"]

        if self.program:
            from datetime import date

            today = date.today()

            age = today.year - dob.year - (
                (today.month, today.day) < (dob.month, dob.day)
            )

            if age < self.program.age_min or age > self.program.age_max:
                raise forms.ValidationError(
                    f"This program is for ages "
                    f"{self.program.age_min}-{self.program.age_max}."
                )

        return dob