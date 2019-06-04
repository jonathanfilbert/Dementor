from django.db import models
import datetime


# Create your models here.
CATEGORY_CHOICES = [("Design", "Design"), ("Development", "Development"), ("Social",
                                                                           "Social"), ("Leadership", "Leadership")]
class PortofolioData(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    short_description = models.CharField(max_length=50)
    description = models.TextField()
    image = models.FileField()

class WhatAmIDoing(models.Model):
    time = models.DateField(default=datetime.date.today)
    update = models.CharField(max_length=200)
