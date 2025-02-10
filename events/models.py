from django.db import models


class Event(models.Model): 
    title = models.CharField(max_length=200) 
    date = models.DateTimeField(max_length=200)
    registration_fee = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    location = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    croppedImage = models.ImageField(upload_to='images/', blank=True, null=True)
    deleted = models.BooleanField(default=False)
    is_tour = models.BooleanField(default=False)
    is_event = models.BooleanField(default=False)
    url = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title
    
    
    
    
    
    
    
    
    
class Participant(models.Model): 
    first_name = models.CharField(max_length=200) 
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200) 
    date_of_birth = models.DateField(max_length=200) 
    email = models.EmailField()
    school_name = models.CharField(max_length=200,null=True, blank=True)

    years_of_training = models.IntegerField(null=True, blank=True)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    
    payment_id = models.CharField(max_length=255) 
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    