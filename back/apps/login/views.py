from django.shortcuts import render

from .forms import RegistrationForm

import psycopg2

def login_page(request):

    return render(request, 'login-page.html')


def registration_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            agreement = request.POST.get('agreement')
            print('AFTER', username, email, password, agreement)
            return render(request, 'login-page.html')
        # TODO Подключить PostgreSQL

    else:
        form = RegistrationForm()
    return render(request, 'registration-page.html', {'form':form})