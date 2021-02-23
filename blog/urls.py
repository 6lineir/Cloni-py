from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    path('', BlogList.as_view(), name='Home'),
    path('<slug:slug>', BlogDetail.as_view(), name='BlogDetail'),

]
