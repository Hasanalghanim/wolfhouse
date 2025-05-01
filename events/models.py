from django.db import models
from ckeditor.fields import RichTextField
from itertools import combinations


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
    rules = RichTextField(default="No rules specified")

    def __str__(self):
        return self.title





class Division(models.Model):
    event = models.ForeignKey(Event, related_name='divisions', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.event.title}"

    def generate_matches(self):
        participants = list(self.participants.filter(deleted=False))
        for p1, p2 in combinations(participants, 2):
            Match.objects.create(division=self, participant1=p1, participant2=p2)

    def generate_matches_with_rounds(self):
        self.matches.all().delete()
        participants = list(self.participants.filter(deleted=False).order_by('id'))
        num_participants = len(participants)

        if num_participants < 2:
            return  # Not enough participants

        if num_participants % 2 == 1:
            participants.append(None)  # Add a bye

        num_rounds = len(participants) - 1
        mid = len(participants) // 2

        for round_number in range(num_rounds):
            for i in range(mid):
                p1 = participants[i]
                p2 = participants[-(i + 1)]

                Match.objects.create(
                    division=self,
                    participant1=p1,
                    participant2=p2,
                    round_number=round_number + 1
                )

            # Rotate (except the first element)
            first = participants[0]
            rest = participants[1:]
            rest = [rest[-1]] + rest[:-1]
            participants = [first] + rest


    def get_winner(self):
        return self.participants.order_by('-points').first()






class Participant(models.Model): 
    first_name = models.CharField(max_length=200) 
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200) 
    date_of_birth = models.DateField(max_length=200) 
    email = models.EmailField()
    school_name = models.CharField(max_length=200,null=True, blank=True)

    years_of_training = models.IntegerField(null=True, blank=True)
    payment_id = models.CharField(max_length=255,null=True, blank=True) 
    weight = models.IntegerField(null=True, blank=True)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    division = models.ForeignKey(Division, related_name='participants', on_delete=models.SET_NULL, null=True, blank=True)
    points = models.IntegerField(default=0)
    
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def update_points(self):
        from .models import Match
        wins = Match.objects.filter(winner=self).count()
        self.points = wins
        self.save(update_fields=['points'])
    

class Match(models.Model):
    division = models.ForeignKey(Division, related_name='matches', on_delete=models.CASCADE)
    participant1 = models.ForeignKey(Participant, related_name='red', on_delete=models.CASCADE,null=True, blank=True)
    participant2 = models.ForeignKey(Participant, related_name='blue', on_delete=models.CASCADE,null=True, blank=True)
    winner = models.ForeignKey(Participant, null=True, blank=True, related_name='won_matches', on_delete=models.SET_NULL)
    round_number = models.IntegerField(default=1) 

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # After saving, update points for both participants
        if self.participant1:
            self.participant1.update_points()
        if self.participant2:
            self.participant2.update_points()

    def __str__(self):
        p1 = self.participant1 if self.participant1 else "No Participant"
        p2 = self.participant2 if self.participant2 else "No Participant"
        return f"{p1} vs {p2} ({self.division.name})"
