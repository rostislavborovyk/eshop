from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User
from .utils import UserGenders


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    gender = forms.ChoiceField(choices=UserGenders.choices())

    class Meta:
        fields = ["username", "email", "gender", "password1", "password2"]
        model = User
