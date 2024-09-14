from django import forms
from django.core import validators


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', required=True, validators=[validators.EmailValidator('Email is incorrect')], widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '***'}))
    agreement = forms.BooleanField(label='Terms and Conditions agreement', required=True, widget=forms.CheckboxInput(attrs={'class': 'form-check', 'id':'agreement'}))
    # agreement = forms.CheckboxInput(attrs={'class': 'form-control'})




class LoginForm(forms.Form):
    username = forms.CharField(label='Username', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '***'}))
