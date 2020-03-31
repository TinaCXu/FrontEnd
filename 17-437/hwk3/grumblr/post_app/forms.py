from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo

class RegisterForm(forms.Form):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    verify_password = forms.CharField()
    introduction = forms.CharField()

    def clean(self):
        #super(RegistrationForm, self).clean()
        cleaned_data = super().clean()
        password = cleaned_data['password']
        verify_password = cleaned_data['verify_password']

        if password != verify_password:
            raise forms.ValidationError('Make sure password match!')

class LoginForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username','password')

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username','first_name','last_name','password','email')

