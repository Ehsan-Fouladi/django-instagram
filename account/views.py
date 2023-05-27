from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def LoginUser(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Login succese")
                else:
                    return HttpResponse("Error login")
            else:
                return HttpResponse("Invaild User")
    else:
        form = LoginForm()
        return render(request, "account/login.html", {'form': form})
@login_required
def Profile(reqeust):
    return render(reqeust, "account/profile.html", {})