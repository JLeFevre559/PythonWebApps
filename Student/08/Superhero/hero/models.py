from django.db import models
from django.contrib.auth.models import User

class Superhero(models.Model):
    name = models.CharField(max_length=200)
    identity = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=200)
    strengths = models.CharField(max_length=200)
    weaknesses = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=200)
    date = models.DateField()
    image = models.CharField(max_length=200)
    hero = models.ForeignKey(Superhero, on_delete=models.CASCADE)
    Investigator = models.ForeignKey(Investigator, on_delete=models.CASCADE)

class Investigator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)