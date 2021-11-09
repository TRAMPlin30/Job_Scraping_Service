from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.forms import UserLoginForm, UserRegistrationForm


def login_views(request):

    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        data = form.cleaned_data
        email = data.get('email') # вытаскиваем данные из тех данных которые поступают к нам в форму
        password = data.get('password') # вытаскиваем данные из тех данных которые поступают к нам в форму
        #user = form.save()
        user = authenticate(request, email=email, password=password)
        login(request, user)

        return redirect('/scraping')

    return render(request, "login_form.html", {'form':form})


def logout_views(request):
    logout(request)
    return redirect('/scraping/')

        # username = request.POST['username'] # вытаскиваем username из request
        # password = request.POST['password'] # вытаскиваем password из request


def register_views(request):
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False) # commit - подготовка к зашифровке пароля (по умолчанию True)
        new_user.set_password(form.cleaned_data['password']) # метод зашифровки пароля
        new_user.save()
        return render(request, 'register_done.html', {'new_user':new_user})
    return render(request, "register_form.html", {'form': form})




