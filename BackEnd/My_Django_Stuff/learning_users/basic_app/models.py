from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    # OneToOneField relationship:a class to add information that default User doesn't have
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # user has one to one relationship with User

    # additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username