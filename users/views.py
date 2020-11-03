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
    # print(request.user.is_authenticated)
    # if request.user.is_authenticated:
    #     current_user = User.objects.get(pk=request.user.pk)
    #     print(current_user)
    #     print(current_user.gender)
    #     print(type(current_user))
    return render(request, "users/users.html")
