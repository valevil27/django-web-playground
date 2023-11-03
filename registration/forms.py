from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserWithMailCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Máximo 254 carácteres.")
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")