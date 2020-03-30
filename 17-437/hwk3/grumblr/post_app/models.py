from django.db import models
from django.contrib.auth.models import User
from django import template,templatetags

# Create your models here.

class UserProfileInfo(models.Model):
    user_name = models.CharField(unique=True,max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)    
    
    def __str__(self):
            return self.user_name