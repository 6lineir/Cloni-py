from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import User
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
	ListView,
	CreateView,
	UpdateView,
	DeleteView
)
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token
from .forms import EditProfileForm, SignupForm

from vertify.models import UserProfile
# Success Ok Request Users 
def Success(request):
    return render(request, "registration/pop/success.html")

# Index Accounts 
def index(request):
    return render(request, "registration/index.html")


# Edite Profile By From
@login_required
def profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
            return redirect('accounts:vertifyAcc')
        else:
            print("Error Save EditeProfiel")
    else:
        form = EditProfileForm(instance=request.user)
        args = { 'from': form}
    return render(request, "registration/profile.html", args)

# VertiFy Accounts Form
class vertifyAcc(LoginRequiredMixin, CreateView):
    model = UserProfile
    fields = [
        "imageAcc",
        "imageCode",
    ]
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def form_invalid(self, form):
        return super().form_invalid(form)
    success_url = reverse_lazy('accounts:success')
    template_name = "registration/vertify-Acc.html"

# Login System Fixed**
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

# Logout System Fexed**
def logout(request):
    if request.method == 'GET':
        auth.logout(request)
    return redirect('blog:Home')

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from .tokens import account_activation_token
# Signup System
class signup(CreateView):
    form_class = SignupForm
    template_name = "registration/signup.html"
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'فعال سازی حساب کاربری'
        massage = render_to_string('registration/acc_activate.html',{
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, massage, to=[to_email]
        )
        email.send()
        return HttpResponse('لینک فعال سازی برای ایمیل شما ارسال شد.')
# Activations Account Link Chek And Create Token Api
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        this_Token = Token.objects.get_or_create(user=user) #Create Auto Token User
        user.save()
        return HttpResponse('حساب کاربری با موفقیت فعال شد  <a href="/accounts/login/">ورود</a>')
    else:
        return HttpResponse('لینک فعال سازی منقضی شده  <a href="/accounts/login/">ورود</a>')
