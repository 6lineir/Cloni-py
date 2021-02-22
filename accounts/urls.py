from django.contrib.auth import views
from django.urls import path
from .views import *

app_name = 'accounts'
urlpatterns = [
    path('', index, name="indexAcc"),
    path('profile/', profile, name="profile"),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout')

]
# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']