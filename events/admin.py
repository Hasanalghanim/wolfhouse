from django.contrib import admin
from .models import Event, Division, Participant, Match
from django import forms

class MatchInlineForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # If this form is for an existing Match instance
        if self.instance and self.instance.pk:
            participants = [
                self.instance.participant1,
                self.instance.participant2,
            ]
            self.fields['winner'].queryset = Match._meta.get_field('winner').remote_field.model.objects.filter(pk__in=[p.pk for p in participants])
        else:
            # For new matches, don't show anything yet
            self.fields['winner'].queryset = Match._meta.get_field('winner').remote_field.model.objects.none()

class MatchInline(admin.TabularInline):
    model = Match
    extra = 0  # No blank rows shown by default
    form = MatchInlineForm
    fields = ('participant1', 'participant2', 'winner')

class ParticipantInline(admin.TabularInline):
    model = Participant
    extra = 0
    fields = ('first_name', 'last_name', 'points')
    readonly_fields = ('points',)



@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('name', 'event', 'division_winner')
    actions = ['generate_round_robin_matches','generate_round_robin_matches_with_rounds']
    inlines = [ParticipantInline, MatchInline]
    def generate_round_robin_matches(self, request, queryset):
        for division in queryset:
            division.generate_matches()
        self.message_user(request, "Round-robin matches generated successfully.")

    def generate_round_robin_matches_with_rounds(self, request, queryset):
        for division in queryset:
            division.generate_matches_with_rounds()
        self.message_user(request, "Round-robin matches generated successfully.")   
    generate_round_robin_matches.short_description = "Generate round-robin matches"

    def division_winner(self, obj):
        winner = obj.get_winner()
        return winner if winner else "TBD"

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'city')

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'event', 'division', 'points')

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('division', 'participant1', 'participant2', 'winner')
