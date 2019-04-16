from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    # fname = models.CharField(max_length=200)
    # lname = models.CharField(max_length=200)
    # username = models.CharField(max_length=200)
    # password = models.CharField(max_length=200)
    age = models.PositiveIntegerField(null = True)
    address = models.TextField()
    pincode = models.PositiveIntegerField(null=True)
    phone = models.PositiveIntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
