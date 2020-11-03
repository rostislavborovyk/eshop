from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate

from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/users")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", context={"form": form})


def users(request):
    # print(request.user.is_authenticated)
    return render(request, "users/users.html")
