# Generated by Django 5.1.4 on 2024-12-17 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_event_fee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='fee',
        ),
    ]