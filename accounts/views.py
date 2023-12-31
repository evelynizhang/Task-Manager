from django.shortcuts import render, redirect
from accounts.forms import LoginForm, SignupForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User


def view_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(
                request,
                username=username,
                password=password,
            )
            if user is not None:
                login(request, user)
                return redirect("list_projects")
            else:
                form.add_error("username", "Login does not seem to work")
    else:
        form = LoginForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


def view_logout(request):
    logout(request)
    return redirect("login")


def view_signupform(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            password_confirmation = request.POST["password_confirmation"]
            if password == password_confirmation:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                )
                login(request, user)
                return redirect("list_projects")
            else:
                form.add_error("password", "passwords do not match")
    else:
        form = SignupForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)
