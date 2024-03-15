from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager

# Если хотим, к Джанговскому стандартному юзеру что-то добавить, то используем AbstractUser
# Если хотим, создать юзера с 0, то используем AbstractBaseUser


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)  # unique=True - Означает что все записи уникально
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
