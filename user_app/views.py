from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import redirect
import requests
import json


def homeView(request):
    print(request.META.get('REMOTE_ADDR'))

    import os
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.environ.get('WEATHER_API_KEY')
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=Almaty"
    response = requests.get(url)
    context = {}
    if response.status_code == 200:
        data = json.loads(response.text)
        context.update({'temp': data['current']['temp_c']})
    return render(request, 'home_template.html', context=context)


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


def productCreateView(request):
    if request.method == 'GET':
        return render(request, 'product_create_template.html')
    elif request.method == 'POST':
        from .models import Product
        product_name = request.POST.get('product_name').capitalize()
        product_price = float(request.POST.get('product_price'))
        product_color = request.POST.get('product_color').capitalize()
        product_quantity = request.POST.get('product_quantity')
        if product_quantity:
            product_quantity = int(product_quantity)
            new_product = Product(name=product_name,
                                  price=product_price,
                                  color=product_color,
                                  quantity=product_quantity)
        else:
            new_product = Product(name=product_name,
                                  price=product_price,
                                  color=product_color)
        new_product.save()
        return redirect('home_url')


def productDetailView(request, product_id):
    from .models import Product
    product = Product.objects.get(id=product_id)
    context = {
        'product': product
    }
    return render(request, 'product_detail_template.html', context=context)


def productDeleteView(request, product_id):
    from .models import Product
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('home_url')
