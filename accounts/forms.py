# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserAccount

class UserAccountCreationForm(UserCreationForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'],
    )
    class Meta:
        model = UserAccount
        fields = ('username', 'email', 'phone_number', 'date_of_birth')
        widgets = {'date_of_brith': forms.DateInput()}


class UserAccountChangeForm(UserChangeForm):
    class Meta:
        model = UserAccount
        fields = ('username', 'email', 'phone_number', 'date_of_birth')
