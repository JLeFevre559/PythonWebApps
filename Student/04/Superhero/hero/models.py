from django.db import models

class Superhero(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    identity = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.name  # Make sure to return something meaningful for readability in the admin
