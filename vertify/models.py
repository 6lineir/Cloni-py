from django.db import models
from accounts.models import User
# Create your models here.
class UserProfile(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    imageAcc = models.ImageField(upload_to='Users/%Y/%m/', blank=True)
    imageCode= models.ImageField(upload_to='Users/%Y/%m/', blank=True)