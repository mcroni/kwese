from django.db import models

# Create your models here.

class Contestant(models.Model):
    name = models.CharField(max_length=100)
    votes = models.IntegerField()

    def __str__(self):
        return self.name