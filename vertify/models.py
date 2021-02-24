from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
# Create your models here.
class UserProfile(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length = 16)
    telphone = models.CharField(max_length = 16)
    codeMelli = models.CharField(max_length = 10, unique=True)
    reffrall = models.CharField(max_length = 10, unique=True, default=get_random_string(10).lower(), editable=False)
    imageAcc = models.ImageField(upload_to='Users/%Y/%m/', blank=True)
    imageCode= models.ImageField(upload_to='Users/%Y/%m/', blank=True)
    activeAcc =models.BooleanField(default=False)
    def __str__(self):
        return self.reffrall