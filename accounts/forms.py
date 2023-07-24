# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserAccount

class UserAccountCreationForm(UserCreationForm):
    class Meta:
        model = UserAccount
        fields = ('name', 'email', 'phone_number',)
        # widgets = {'date_of_brith': forms.DateInput()}


class UserAccountChangeForm(UserChangeForm):
    class Meta:
        model = UserAccount
        fields = ('name', 'email', 'phone_number', 'date_of_birth')
