from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView, name='home_url'),
    path('logout', logOutView, name='log_out_url'),
    path('login', logInView, name='log_in_url'),
    path('register', registerView, name='register_url'),
    path('product_create', productCreateView, name='product_create_url'),
    path('product_detail/<int:product_id>', productDetailView, name='product_detail_url'),
    path('product_delete/<int:product_id>', productDeleteView, name='product_delete_url'),
]
