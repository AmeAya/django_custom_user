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


def registerView(request):
    if request.method == 'GET':
        return render(request, 'registration_template.html')
    elif request.method == 'POST':
        from .models import CustomUser
        input_email = request.POST.get('email')
        input_pass1 = request.POST.get('pass1')
        input_pass2 = request.POST.get('pass2')
        this_user = CustomUser.objects.filter(email=input_email)
        if len(this_user) > 0:  # Если найден юзер с таким email. Не дать зарегистрироваться так как email занят
            context = {
                'message': 'This email already taken!'
            }
            return render(request, 'registration_template.html', context=context)
        if input_pass1 != input_pass2:  # Если пароли не сходятся
            context = {
                'message': 'Passwords doesn`t match!',
                'email': input_email
            }
            return render(request, 'registration_template.html', context=context)
        user = CustomUser.objects.create_user(email=input_email, password=input_pass1)
        login(request, user)
        return redirect('home_url')
