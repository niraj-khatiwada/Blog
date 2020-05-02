from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required


def signup(request):
    form = SignUpForm()
    context = {
        "form": form
    }
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get("username")
            messages.success(
                request, f'Account creation successful for {username}')
            return redirect("login")

    return render(request, "accounts/signup.html", context)


@login_required()
def profile(request):
    return render(request, "accounts/profile.html")
