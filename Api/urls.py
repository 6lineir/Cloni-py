from django.urls import path, include
from .views import *

app_name = 'Api'
urlpatterns = [
    path(r'', BlogApi.as_view(), name="blogApi"),
    # path(r'add/', BlogCreateApi.as_view(), name="blogApi"),
    path(r'<int:pk>', PostApi.as_view(), name="blogApi"),
    path(r'users/', UsersApi.as_view(), name="usersApi"),
    path(r'users/<int:pk>', UserApi.as_view(), name="userApi"),
    path(r'login/', LoginApi.as_view(), name='LoginApi'),
    path(r'add/', addAPI.as_view(), name="addApi"),
]
