from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=150)
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    
    def __str__(self) -> str:
        return self.email
    
    class Meta:
        db_table = 'users'
        ordering = ['name']


