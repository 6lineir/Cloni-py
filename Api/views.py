from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import BlogSerializer, UsersSerializer
from blog.models import Blog



# /api/
class BlogApi(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
# /api/<id>
class PostApi(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer



from django.contrib.auth.models import User
# /api/users/
class UsersApi(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
# /api/users/<pk>
class UserApi(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer