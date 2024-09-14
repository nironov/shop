from django import forms
from django.core.mail import send_mail
from django.core import validators


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', required=True, validators=[validators.EmailValidator('Email is incorrect')], widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '***'}))
    agreement = forms.BooleanField(label='Terms and Conditions agreement', required=True, widget=forms.CheckboxInput(attrs={'class': 'form-check', 'id':'agreement'}))

    #TODO: Подключить celery
    def send_confirmation_email(self):
        send_mail('Confirmation', f'Dear {self.username}, Thank you for using our service', 'admin@mysite.com', [self.email], fail_silently=False)




class LoginForm(forms.Form):
    username = forms.CharField(label='Username', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '***'}))
