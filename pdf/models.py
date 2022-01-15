from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)
    summary = models.TextField(max_length=5000)
    degree = models.CharField(max_length=500)
    class10 = models.CharField(max_length=500)
    class12 = models.CharField(max_length=500)
    university = models.CharField(max_length=500)
    previous_work = models.TextField(max_length=5000)
    skills = models.TextField(max_length=1000)
    projects = models.TextField(max_length=5000)





