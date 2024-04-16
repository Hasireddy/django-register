from django.shortcuts import render

# from . import forms
from .forms import RegisterForm
from .models import Register

# Create your views here.


def register(request):
    form = RegisterForm()
    return render(request, "signupForm/register.html", {"form": form})
