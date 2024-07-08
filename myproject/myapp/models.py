from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=50)
    number = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

class Game(models.Model):
    number = models.IntegerField()
    player_name = models.CharField(max_length=255)
    number_of_guesses = models.IntegerField(default=0)