from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class EditProfileForm(forms.ModelForm):
  class Meta:
    model = User
    fields = (
      "last_name",
      "first_name",
      "email",
    )

# class VertifyPhoneForm(forms.ModelForm):
#     class Meta:
#       model = UserProfile
#       fields = (
#         "phone"
#         "telphone"
#       )
from vertify.models import UserProfile
class VertifyAccForm(forms.ModelForm):
    class Meta:
      model = UserProfile
      fields = (
        "codeMelli",
        "imageAcc",
        "imageCode",
      )