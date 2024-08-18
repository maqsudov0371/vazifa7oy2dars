from django.db import models
from django.contrib.auth.models import AbstractUser, User
# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=13, blank=True, unique=True, db_index=True)
    auth_code = models.CharField(max_length=6, blank=True) 

    def __str__(self) -> str:
        return f"{self.username}"
    

