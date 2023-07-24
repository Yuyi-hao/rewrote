from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.

class UserAccount(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    joining_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    
