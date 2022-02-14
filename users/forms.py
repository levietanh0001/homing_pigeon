from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import CustomUser




class CustomUserLoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields=('email', 'password')