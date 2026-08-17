from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RegistrationForm
from .models import Program


def programs(request):
    programs = Program.objects.filter(
        registration_open=True
    )

    return render(
        request,
        "programs.html",
        {"programs": programs}
    )


def program_detail(request, slug):
    program = get_object_or_404(
        Program,
        slug=slug
    )

    return render(
        request,
        "program_detail.html",
        {"program": program}
    )


def program_register(request, slug):
    program = get_object_or_404(
        Program,
        slug=slug
    )

    if not program.registration_open:
        return render(
            request,
            "registration_closed.html",
            {"program": program}
        )

    if program.is_full:
        return render(
            request,
            "program_full.html",
            {"program": program}
        )

    if request.method == "POST":

        form = RegistrationForm(
            request.POST,
            program=program
        )
        print(form.errors)
        if form.is_valid():

            registration = form.save(commit=False)
            registration.program = program
            registration.save()

            send_mail(
                subject=f"Wolfhouse MMA Registration - {program.name}",
                message=(
                    f"Thank you for registering {registration.child_name} "
                    f"for the {program.name}.\n\n"
                    f"We have received your registration and will contact "
                    f"you with the next steps."
                ),
                from_email=None,
                recipient_list=[registration.parent_email],
                fail_silently=True,
            )

            return redirect(
                "registration_success",
                registration_id=registration.id
            )

    else:
        form = RegistrationForm(
            program=program
        )

    return render(
        request,
        "register.html",
        {
            "program": program,
            "form": form,
        }
    )


def registration_success(request, registration_id):
    return render(
        request,
        "registration_success.html",
        {"registration_id": registration_id}
    )