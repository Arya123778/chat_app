from django.contrib.auth.models import AbstractUser
from django.db import models 
# Create your models here.
class User(AbstractUser):
    email=models.EmailField(unique=True)
    bio=models.TextField(blank=True, null=True)
    avatar=models.ImageField(upload_to='avatars/', blank=True, null=True)
    is_online=models.BooleanField(default=False)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']