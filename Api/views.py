from django.shortcuts import render, get_object_or_404
from .serializers import BlogSerializer, UsersSerializer, addSerial, LoginSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from blog.models import Blog, Category
from accounts.models import User


class LoginApi(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer


class addAPI(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = addSerial
    permission_classes = (IsAuthenticated,)
    


# /api/
class BlogApi(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
# /api/<id>
class PostApi(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
class BlogCreateApi(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


from accounts.models import User
# /api/users/
class UsersApi(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
# /api/users/<pk>
class UserApi(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer