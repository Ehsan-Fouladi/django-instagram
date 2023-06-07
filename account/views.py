from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm, ProfileForms, VerifyCodeForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from random import randint


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


def Register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data["password"]
            password2 = form.cleaned_data["password2"]
            phone = form.cleaned_data['phone']
            if password == password2:
                user.set_password(password)
            else:
                form = RegisterForm(initial={'phone': phone})
                messages.error(request, "password dosn`t match!")
                return render(request, "account/register.html", {"form": form})
            user.save()
            login(request, user)
            verify_code = randint(11111, 99999)
            request.session["verify"] = verify_code
            print(request.session["verify"])
            return redirect("verify_register")
    else:
        form = RegisterForm()
    return render(request, "account/register.html", {"form": form})


def Verify_Register(request):
    if request.method == "POST":
        form = VerifyCodeForm(request.POST)
        if form.is_valid():
            verify_code = form.cleaned_data["code"]
            if verify_code == request.session["verify"]:
                user = request.user
                user.is_verify = True
                user.save()
                return redirect("profile")
            else:
                messages.error(request, "Code is Invalid")
    else:
        form = VerifyCodeForm()
        return render(request, "account/verify.html", {"form": form})


@login_required
def Profile(reqeust):
    return render(reqeust, "account/profile.html", {})


@login_required
def ProfileEdit(reqeust):
    if reqeust.method == "POST":
        form = ProfileForms(instance=reqeust.user, data=reqeust.POST, files=reqeust.FILES)
        if form.is_valid():
            form.save()
            messages.success(reqeust, "Edit Profile successfully")
            return redirect('profile')
        else:
            messages.error(reqeust, "Error Updating Your Profile")
    else:
        form = ProfileForms(instance=reqeust.user)
    return render(reqeust, "account/edit_profile.html", {"form": form})
