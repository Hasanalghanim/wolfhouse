# Generated by Django 4.1.3 on 2024-07-08 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_rename_coaches_coach'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='bio',
            field=models.CharField(default='', max_length=500),
        ),
    ]