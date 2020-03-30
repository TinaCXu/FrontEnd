from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo
from django import template,templatetags

class UserForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('user_name','first_name','last_name','password')