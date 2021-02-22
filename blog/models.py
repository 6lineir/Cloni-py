from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Model CateGory Fr Blog
class Category(models.Model):
    title = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 50)
    def __str__(self):
        return self.title


# Models Blog Posts
class Blog(models.Model):
    STATUS_CHOICES = (
        ('n', 'جدید'),		     # new
        ('i', "در حال بررسی"),	 # investigation
        ('p', "انتشار یافته"),	 # publish
        ('b', "بایگانی"),        # Close
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 50)
    status = models.CharField(max_length=5, choices=STATUS_CHOICES)
    body = models.TextField()
    image = models.ImageField(upload_to='blog/%Y/%m/', blank=True)
    public = models.BooleanField(default=False)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    