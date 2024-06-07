from django.db import models

# Create your models here.

class Membership(models.Model):
    title  = models.CharField(max_length=200)
    monthly = models.DecimalField(max_digits=7, decimal_places=2)
    yearly = models.DecimalField(max_digits=7, decimal_places=2)
    extraDetail = models.CharField(max_length=500)
