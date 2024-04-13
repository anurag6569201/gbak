from django.db import models

# Create your models here.
class blog(models.Model):
    textarea=models.CharField(max_length=1000)
    heading=models.CharField(max_length=100)