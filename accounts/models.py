from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models 


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=150, blank=True, null=True)
    email=models.EmailField(unique=True)
    bio=models.TextField(blank=True, null=True)
    avatar=models.ImageField(upload_to='avatars/', blank=True, null=True)
    is_online=models.BooleanField(default=False)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
