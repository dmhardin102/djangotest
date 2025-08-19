from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Document


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ("title", "file")
