from django.shortcuts import render, redirect
from accounts.forms import LoginForm
from django.contrib.auth import login, authenticate


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
