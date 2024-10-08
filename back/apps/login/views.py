from django.shortcuts import render, redirect

from .forms import RegistrationForm, LoginForm
from .utils import validate_jwt_token, check_user_exists_in_db
from apps.core.postgresql_connection import cur, conn


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username: str = request.POST.get('username')
            password: str = request.POST.get('password')
            user = check_user_exists_in_db(username) # (6, 'user2', '333444', 'user2@gmail.com') <class 'tuple'>
            print('USER LOGIN PAGE', user)
            if not user['exists']:
                return render(request, 'login-page.html', {'form':form, 'message':f'There is no user with username: {username}'})

            if password == user['password']:
                print('LOGIN ACCEPTED')
                return redirect('index')
            else:
                print('ACCESS DENIED')
                return render(request, 'login-page.html', {'form':form, 'message':f'either username or password is invalid'})


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
            user = check_user_exists_in_db(username, email)

            if user['exists']:
                return render(request, 'registration-page.html', {'form':form, 'message': f'user {username} already taken'})

            else:
                form.send_confirmation_email(username, email)
                cur.execute(f"INSERT INTO users (username, password, email) VALUES ('{username}', '{password}', '{email}')")
                conn.commit()
                # Перенаправлять юзера на страницу заглушку в ожидании подтверждения email
                # ИЛИ
                # Дать доступ к приложению, но требовать подтверждения email
                return render(request, 'index.html')

    if request.method == 'GET':
        if request.GET.get('token'):
            jwt_token = request.GET.get('token')
            if validate_jwt_token(jwt_token):
                return render(request, 'index.html')
            form = RegistrationForm()
            return render(request, 'registration-page.html', {'form':form, 'message':'link is expired'})

        else:
            form = RegistrationForm()
    return render(request, 'registration-page.html', {'form':form})


