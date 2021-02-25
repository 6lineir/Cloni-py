from django.contrib.auth import views
from django.urls import path, re_path
from .views import *
from django.contrib.auth import views as auth_views


app_name = 'accounts'
urlpatterns = [
    path('', index, name="indexAcc"),
    path('success/', Success, name="success"),
    path('vertify/', vertifyAcc.as_view(), name="vertifyAcc"),
    path('profile/', profile, name="profile"),
    path('login/', login, name='login'),
    path('signup/', signup.as_view(), name='signup'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('logout/', logout, name='logout'),
    path('change-password/', auth_views.PasswordChangeView.as_view(), name='password_change')

]
# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']