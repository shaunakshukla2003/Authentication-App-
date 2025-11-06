from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.
class CustomUser(AbstractUser):
    username=None
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True,blank=True)
    address =  models.TextField(null=True,blank=True)
    phone_number = models.CharField(max_length=20,unique=True)
    city = models.CharField(max_length=200)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 
    
    objects = UserManager()
    
    def __str__(self):
        return self.email