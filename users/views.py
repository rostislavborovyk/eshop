from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import RegisterForm
from .models import User


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/users")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", context={"form": form})


def users(request):
    # excluding super user
    users = User.objects.exclude(is_staff=1).all()

    context = {
        "users": users
    }
    return render(request, "users/users.html", context)
