from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'department', 'year', 'section', 'roll_number', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.role == 'student':
            self.fields['year'].required = True
            self.fields['section'].required = True
            self.fields['roll_number'].required = True
        else:
            self.fields['year'].widget = forms.HiddenInput()
            self.fields['section'].widget = forms.HiddenInput()
            self.fields['roll_number'].widget = forms.HiddenInput()

    def clean_username(self):
        username = self.cleaned_data.get('username')
        # Check if the username is different from the current user's username
        if CustomUser.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This username already exists.")
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        if user.role != 'student':
            user.year = None
            user.section = None
        if commit:
            user.save()
        return user
