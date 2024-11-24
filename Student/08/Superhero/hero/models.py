from django.db import models
from django.contrib.auth.models import User

class Superhero(models.Model):
    name = models.CharField(max_length=200)
    identity = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ForeignKey('Photo', on_delete=models.CASCADE, null=True, blank=True)
    strengths = models.CharField(max_length=200)
    weaknesses = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Investigator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=200)
    date = models.DateField()
    image = models.ForeignKey('Photo', on_delete=models.CASCADE, null=True, blank=True)
    hero = models.ForeignKey(Superhero, on_delete=models.CASCADE)
    Investigator = models.ForeignKey(Investigator, on_delete=models.CASCADE, null=True, blank=True)

def get_upload(instance, filename):
        return f'images/{filename}'

class Photo(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to=get_upload)

    def __str__(self):
        return self.title

    

