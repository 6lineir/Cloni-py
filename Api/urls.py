from django.urls import path, include
from .views import *

app_name = 'Api'
urlpatterns = [
    path(r'', BlogApi.as_view(), name="blogApi"),
    path(r'<int:pk>', PostApi.as_view(), name="blogApi"),
    path(r'users/', UsersApi.as_view(), name="usersApi"),
]
