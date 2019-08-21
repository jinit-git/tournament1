from django.db import models

# Create your models here.

class matchez(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    efees = models.IntegerField()
    winpz = models.IntegerField()
