from django.contrib import admin
from .models import Program, Registration


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "age_min",
        "age_max",
        "price",
        "capacity",
        "registration_count",
        "spots_remaining",
        "registration_open",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    list_filter = (
        "registration_open",
    )


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = (
        "child_name",
        "program",
        "parent_name",
        "parent_email",
        "status",
        "created_at",
    )

    list_filter = (
        "program",
        "status",
        "created_at",
    )

    search_fields = (
        "child_name",
        "parent_name",
        "parent_email",
        "parent_phone",
    )

    readonly_fields = (
        "created_at",
    )

    list_editable = (
        "status",
    )