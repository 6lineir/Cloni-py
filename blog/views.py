from django.shortcuts import render
from .models import Blog
# Create your views here.

def index(request):
    blog = Blog.objects.all()
    context = {
        'blog' : blog
    }
    return render(request, "blog/index.html", context)