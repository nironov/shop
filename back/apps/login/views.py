from django.shortcuts import render

from .forms import RegistrationForm

import psycopg2
import bcrypt

def login_page(request):

    return render(request, 'login-page.html')


def registration_page(request):
    conn = psycopg2.connect('dbname=shopdb user=postgres password=123')
    cur = conn.cursor()

    if request.method == 'POST':


        form = RegistrationForm(request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            agreement = request.POST.get('agreement')
            print('AFTER', type(username), email, password, agreement)

            hashed_password = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
            print('HASHED PASSWORD', hashed_password, type(hashed_password))

            cur.execute(f"INSERT INTO users (username, password, email) VALUES ('{username}', '{hashed_password}', '{email}')") # TODO добавить захешированный пароль в БД
            conn.commit()
            return render(request, 'login-page.html')


    else:
        form = RegistrationForm()

        cur.execute('select * from users;')

        print(cur.fetchall())
    return render(request, 'registration-page.html', {'form':form})