from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string
class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='ایمیل')
    phone = models.CharField(max_length = 16, verbose_name='موبایل')
    codeMelli = models.CharField(max_length = 10, unique=True, verbose_name='کد ملی')
    reffrall = models.CharField(max_length = 10, unique=True, default=get_random_string(10).lower(), editable=False, verbose_name='کد بازاریابی')
    is_author = models.BooleanField(default=False, verbose_name="کاربر تایید شده")