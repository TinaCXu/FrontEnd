from django import forms
from django.core import validators
from AppTwo.models import User

class FormName(forms.ModelForm):
    # collect model to the form fields
    class Meta():
        model = User
        fields = "__all__"
        # include all model-user fields into the from fields
        # ["field1","field2"]: exclude certain fields
        # ("field1","field2"): include certain fields

