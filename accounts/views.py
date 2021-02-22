from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
	ListView,
	CreateView,
	UpdateView,
	DeleteView
)
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# from .forms import EditProfileForm , VertifyForm
from rest_framework.authtoken.models import Token



# Success Ok Request Users 
def Success(request):
    return render(request, "registration/success.html")

# Index Accounts 
def index(request):
    return render(request, "registration/index.html")

# 
# def profile(request):
#     if request.method == "POST":
#       form = EditProfileForm(request.POST, instance=request.user)
#       if form.is_valid:
#         form.save()
#         return redirect('accounts:profile')
#     else:
#       form = EditProfileForm(instance=request.user)
#       args = {'form': form}
#     return render(request, "registration/profile.html", args )
#
from .forms import EditProfileForm
@login_required
def profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
            return redirect('accounts:success')
        else:
            print("Error Save EditeProfiel")
    else:
        form = EditProfileForm(instance=request.user)
        args = { 'from': form}
    return render(request, "registration/profile.html", args)

# Login System Fixed
def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:profile')
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('accounts:profile')
        else:
            return render(request,'registration/login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'registration/login.html')

# Logout System Fexed
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('blog:Home')


# Signup System
def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:profile')
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'registration/signup.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                token = Token.objects.get_or_create(user=user) #Create Auto Token User
                auth.login(request,user)
                return redirect('accounts:indexAcc')
        else:
            return render (request,'registration/signup.html', {'error':'Password does not match!'})
    else:
        return render(request,'registration/signup.html')




# def vertifyAccount(request):
#     if request.method == "POST":
#       form = VertifyForm(request.POST, request.FILES, instance=request.user )
#       if form.is_valid():
#         form.save()
#         return redirect('accounts:vertify')
#     else:
#       form = VertifyForm(instance=request.user)
#       args = {'form': form}
#     return render(request, "registration/vertify.html", args)
