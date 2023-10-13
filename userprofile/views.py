from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import *
from .models import *


@login_required(login_url='login')
def home(request):
    active_users = User.objects.filter(is_active=True)
    return render(request, 'userprofile/home.html', {'active_users': active_users})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')

    else:
        form = AuthenticationForm()

    return render(request, 'userprofile/login.html', {'form': form})


def Userlogout(request):
    logout(request)
    return redirect('login')


def registration(request):
    userform = UserForm()
    userprofile = UserProfileForm()

    if request.method == 'POST':
        userform = UserForm(request.POST)
        userprofile = UserProfileForm(request.POST)
        if userform.is_valid() and userprofile.is_valid():  
            password = userform.cleaned_data.get('password')
            address = userprofile.cleaned_data.get('address')
            user = userform.save(commit=False)
            user.set_password(password)
            
            user.save()
            profile = userprofile.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            print(password,address)
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please correct the errors.')

    return render(request, 'userprofile/registration.html', {'user_form': userform, 'user_profile': userprofile})
