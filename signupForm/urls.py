from django.urls import path
from . import views

urlpatterns = [
    path("", views.register, name="register"),
    path("form-submitted/", views.form_submitted, name="form-submitted"),
    path("home/", views.home, name="home"),
    path("login/", views.login, name="login"),
]
