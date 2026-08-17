from django.db import models
from ckeditor.fields import RichTextField


class Program(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = RichTextField()
    age_min = models.PositiveIntegerField()
    age_max = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    schedule = RichTextField()
    location = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField(default=20)
    registration_open = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def registration_count(self):
        return self.registrations.filter(
            status__in=["pending", "confirmed"]
        ).count()

    @property
    def spots_remaining(self):
        return max(0, self.capacity - self.registration_count)

    @property
    def is_full(self):
        return self.spots_remaining <= 0

    def __str__(self):
        return self.name


class Registration(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("waitlist", "Waitlist"),
        ("cancelled", "Cancelled"),
    ]

    program = models.ForeignKey(
        Program,
        on_delete=models.PROTECT,
        related_name="registrations"
    )

    parent_name = models.CharField(max_length=200)
    parent_email = models.EmailField()
    parent_phone = models.CharField(max_length=30)

    child_name = models.CharField(max_length=200)
    child_dob = models.DateField()

    emergency_contact = models.CharField(max_length=200)
    emergency_phone = models.CharField(max_length=30)

    additional_information = models.TextField(blank=True)

    waiver_accepted = models.BooleanField(default=False)
    terms_accepted = models.BooleanField(default=False)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.child_name} - {self.program.name}"