from django.db import models
from django.contrib.auth.models import User
from django import template,templatetags

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, default=None)
    introduction = models.TextField(max_length=500, blank=False, null=False, default='INTRODUCTION')
    def __str__(self):
        return self.user.username