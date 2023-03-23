"""
ModelForms for Accounts App
"""

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms

User = get_user_model()


class RegisterUserForm(UserCreationForm):
    """
    ModelForm for User Registration
    """
    class Meta:
        """
        Meta class for RegisterUserForm
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']
