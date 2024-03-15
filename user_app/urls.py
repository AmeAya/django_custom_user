from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView, name='home_url'),
    path('logout', logOutView, name='log_out_url'),
    path('login', logInView, name='log_in_url'),
    path('register', registerView, name='register_url'),
]
