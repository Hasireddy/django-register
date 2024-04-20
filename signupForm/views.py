from django.shortcuts import render, redirect, HttpResponseRedirect

# from . import forms
from .forms import RegisterForm
from .forms import LoginForm
from .models import Register
from .models import Login

# Create your views here.


# def register(request):
#     form = RegisterForm()
#     return render(request, "signupForm/register.html", {"form": form})


def register(request):
    # If it is a post method render this code
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = Register(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password1=form.cleaned_data["password1"],
                password2=form.cleaned_data["password2"],
            )
            # Check if user already exists
            # user = Register.objects.filter(Email=email)
            # if user:
            #     message = "User already exists"
            #     return render(request, "signupForm/register1.html", {"msg": message})
            # print(form.cleaned_data["first_name"])
            # print(registered_values.first_name)
            user.save()
            # if data is valid save it and redirect it to the success page
            # return redirect("/form-submitted/")
            # message = "user registered successfully"
            # return render(request, "signupForm/login.html", {"msg": message})
            return HttpResponseRedirect("/form-submitted")
        else:
            return render(request, "signupForm/register1.html", {"form": form})
        # If the form is not valid render the form with inputs given by User already,so that he wont loose the information he entered. User entered information will be stored in form = RegisterForm(request.POST). So returning the same form for the User

    # If it is a get request render this code display the empty register form

    form = RegisterForm()
    return render(request, "signupForm/register1.html", {"form": form})


def form_submitted(request):
    return render(request, "signupForm/form_submitted.html")


def home(request):
    return render(request, "signupForm/home.html")


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            loggedInvalues = Login(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            form.save()
            return redirect("/form-submitted")
        else:
            return render(request, "SignupForm/login.html", {"form": form})
    else:
        form = LoginForm()
        return render(request, "signupForm/login.html")
