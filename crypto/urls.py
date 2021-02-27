from django.urls import path
from .views import *

app_name = 'crypto'
urlpatterns = [
    path('', getdata, name='apidata'),

]
