from django.urls import path
from . import views


urlpatterns = [
    path(
        "",
        views.programs,
        name="programs"
    ),

    path(
        "programs/<slug:slug>/",
        views.program_detail,
        name="program_detail"
    ),

    path(
        "programs/<slug:slug>/register/",
        views.program_register,
        name="program_register"
    ),

    path(
        "programs/registration-success/<int:registration_id>/",
        views.registration_success,
        name="registration_success"
    ),
]