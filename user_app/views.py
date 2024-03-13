from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import redirect


def homeView(request):
    return render(request, 'home_template.html')


def logOutView(request):
    logout(request)
    return redirect('home_url')


def logInView(request):
    if request.method == 'GET':
        return render(request, 'login_template.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        user = authenticate(request, email=email, password=pass1)
        # authenticate если юзер с такими данными есть, то он
        # его возвращает
        # Если такого юзера нету, то возвращает None
        if user is not None:
            login(request, user)
            return redirect('home_url')
        else:
            return redirect('log_in_url')
