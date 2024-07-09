from django.db import models

# Create your models here.

class Membership(models.Model):
    title  = models.CharField(max_length=200)
    monthly = models.DecimalField(max_digits=7, decimal_places=2)
    yearly = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    extraDetail = models.TextField(max_length=500)
    signupFee = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.title




class Training(models.Model):
    title  = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    croppedImage = models.ImageField(upload_to='images/', blank=True, null=True)
    extraDetail = models.TextField(max_length=500,blank=True, null=True)
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.title


class Background(models.Model): 
    title = models.CharField(max_length=200) 
    image = models.ImageField(upload_to='images/')
    croppedImage = models.ImageField(upload_to='images/', blank=True, null=True)
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    



class Coach(models.Model): 
    name = models.CharField(max_length=200) 
    disciple = models.CharField(max_length=500,blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    bio = models.TextField(max_length=1000,blank=True, null=True)
    stats = models.CharField(max_length=500,blank=True, null=True)
    orderNumber = models.IntegerField(blank=True, null=True)
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.name