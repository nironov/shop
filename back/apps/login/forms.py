from django import forms
from django.core import validators


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', required=True, max_length=100)
    email = forms.EmailField(label='Email', required=True, validators=[validators.EmailValidator('Email is incorrect')])
    password = forms.PasswordInput()
    agreement = forms.BooleanField(label='Terms and Conditions agreement', required=True)




# class LoginForm(forms.Form):
