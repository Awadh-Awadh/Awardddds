from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUSer


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUSer
        fields = ('first_name','last_name','username','email')



class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUSer
        fields = ('first_name','last_name','username','email')