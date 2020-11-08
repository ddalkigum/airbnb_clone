import jwt
from django.views import View
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate, logout
from .models import User
from .forms import UserLoginForm


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm
        return render(request, "login.html", context={"form": form})

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("rooms:home")

        return render(request, "users:login", context={"form": form})


def log_out(request):
    logout(request)
    return redirect(reverse("rooms:home"))
