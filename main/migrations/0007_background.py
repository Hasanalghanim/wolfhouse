# Generated by Django 4.1.3 on 2024-06-20 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_membership_yearly'),
    ]

    operations = [
        migrations.CreateModel(
            name='Background',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
                ('croppedImage', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('deleted', models.BooleanField()),
            ],
        ),
    ]
