from django.db import models

# Create your models here.
class schoolnums(models.Model):
    numberOfSchool=models.IntegerField()
    states=models.IntegerField()
    video = models.FileField(upload_to='videos/', null=True, blank=True)

class investor(models.Model):
    invName=models.CharField(max_length=50)
    invDonationTime=models.CharField(max_length=50)
    invMoney=models.CharField(max_length=10)
    invPurpose=models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='investors/',null=True, blank=True)

class homePageImage(models.Model):
    images = models.ImageField(upload_to='HomeImages/',null=True, blank=True)