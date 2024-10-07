from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

# Custom form for user registration (extends Django's built-in UserCreationForm)
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']  # Include 'password1' and 'password2' for password confirmation

# Custom form for updating user information (extends Django's built-in UserChangeForm)
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'role']  # Add other fields you need
