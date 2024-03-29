from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import models

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class TweetForm(forms.ModelForm):
    
    class Meta:
        model = models.Tweet
        fields = ("tweet",)