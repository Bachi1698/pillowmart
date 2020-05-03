from django import forms
from django.contrib.auth.models import User 
from . import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 

class RegistrationForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField( max_length=250, required=True)
    model = User
    field = (
        'username',
        'email',
        'first_name',
        'last_name',
        'password1',
        'password2',
    ) 