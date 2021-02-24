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