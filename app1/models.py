from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Application(models.Model):
    name = models.CharField(max_length=250, unique=True)
    email = models.CharField(max_length=250, blank=True,unique=False)
    gender = models.CharField(max_length=250,blank=False)
    age = models.PositiveIntegerField(default=0,blank=True,null=True)
    phone = models.CharField(max_length=12,blank=False)
    dob = models.DateField(blank=False,default=True)
    district = models.CharField(max_length=50,blank=True)
    branch = models.CharField(max_length=50,blank=True)
    acc_type = models.CharField(max_length=20,blank=True)
    materials = models.CharField(max_length=100,blank=True)
    address = models.TextField(blank=False,null=True)
    address_full = models.TextField(blank=False,null=True)
    zip = models.PositiveIntegerField(blank=False,null=False)

    def __str__(self):
        return self.name