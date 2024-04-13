from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
POSITION_CHOICES=(
    ('Member','Member'),
    ('Admin','Admin'),
    ('Volunteer','Volunteer'),
)
class blog(models.Model):
    textarea=CKEditor5Field(config_name='extends')
    heading=models.CharField(max_length=100)

class aboutUs(models.Model):
    textarea=CKEditor5Field(config_name='extends')
    heading=models.CharField(max_length=100)

class teamMembers(models.Model):
    profile_image = models.ImageField(upload_to='members/',null=True, blank=True)
    name=models.CharField(max_length=100)
    position=models.CharField(max_length=100,choices=POSITION_CHOICES)
    sinceJoined=models.DateTimeField(null=True)
    college=models.CharField(max_length=100)

class gallery(models.Model):
    images = models.ImageField(upload_to='gallery/',null=True, blank=True)

class events(models.Model):
    eventDate=models.DateTimeField(null=True)
    heading=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    date=models.DateTimeField(null=True)
    about=models.CharField(max_length=100)
