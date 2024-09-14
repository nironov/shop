from django.shortcuts import render

from .forms import RegistrationForm, LoginForm

import psycopg2


conn = psycopg2.connect('dbname=shopdb user=postgres password=123')
cur = conn.cursor()


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username: str = request.POST.get('username')
            password: str = request.POST.get('password')
            cur.execute(f"select * from users where username = '{username}'")
            password_from_db = cur.fetchone() # (6, 'user2', '333444', 'user2@gmail.com') <class 'tuple'>

            if password == password_from_db[2]:
                print('LOGIN ACCEPTED')
                return render(request, 'registration-page.htmL')
            else:
                print('ACCESS DENIED')

    if request.method == 'GET':
        form = LoginForm()
    return render(request, 'login-page.html', {'form':form})


def registration_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            email = request.POST.get('email')
            password: str = request.POST.get('password')
            agreement = request.POST.get('agreement')
            form.send_confirmation_email()
            cur.execute(f"INSERT INTO users (username, password, email) VALUES ('{username}', '{password}', '{email}')")
            conn.commit()
            return render(request, 'login-page.html')

    else:
        form = RegistrationForm()
        cur.execute('select * from users;')
        print(cur.fetchall())
    return render(request, 'registration-page.html', {'form':form})