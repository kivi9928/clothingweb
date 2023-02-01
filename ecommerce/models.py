from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model
# User = get_user_model()
# Create your models here.

status = [("Active", "Active"), ("Inactive", "Inactive"), ("Delete", "Delete")]
gender = [('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')]

class User(AbstractUser):
     
    email = models.EmailField( null=True)
    phone_no =models.CharField(max_length= 10, null=True)
    city = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=20, null = True)
    image = models.ImageField( upload_to='profile/')
    gender = models.CharField(max_length=10, choices=gender, default='Male')
    dob = models.DateField(null=True, blank=True)
    address = models.CharField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=status, default='Active')
    timestamp = models.DateTimeField(auto_now_add=True)
    utimestamp = models.DateTimeField(auto_now=True)
    track = models.TextField(blank=True, editable=False)
    utrack = models.TextField(blank=True, editable=False)
    
    def __str__(self):
        return self.email

# class Category(models.Model):
#     title = models.CharField(max_length=40)
#     icon = models.ImageField(null=True, blank=True, upload_to='icon/')
#     description = models.TextField(null=True, blank=True)
#     PENDING = 0
#     DONE = 1
#     STATUS_CHOICES = ((PENDING, 'Pending'),(DONE, 'Done'),)
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
#     timestamp = models.DateTimeField(auto_now_add=True)
#     utimestamp = models.DateTimeField(auto_now=True)
#     track = models.TextField(blank=True, editable=False)
#     utrack = models.TextField(blank=True, editable=False)