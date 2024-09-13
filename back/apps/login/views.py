from django.shortcuts import render

from .forms import RegistrationForm


def login_page(request):

    return render(request, 'login-page.html')


def registration_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST) #TODO форма приходит с ошибками
        # print(form)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(username, email, password)
            return 200

    else:
        form = RegistrationForm()
    return render(request, 'registration-page.html', {'form':form})