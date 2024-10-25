from django.db import models


class Superhero(models.Model):
    name = models.CharField(max_length=200)
    identity = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=200)
    strengths = models.CharField(max_length=200)
    weaknesses = models.CharField(max_length=200)

# Create your models here.
