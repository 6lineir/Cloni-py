from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Blog
# Create your views here.

class BlogList(ListView):
    def get_queryset(self):
        return Blog.objects.filter(public=True)

class BlogDetail(DetailView):
    def get_queryset(self):
        return Blog.objects.filter(public=True)
