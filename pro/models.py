from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    USER = (
        ('A', 'ADMIN'),
        ('B', 'EDITOR'),
        ('C', 'USER')
    )
    user_type=models.CharField(choices=USER, max_length=100, default='C')
    user_profile=models.ImageField(upload_to='profile_pic')
