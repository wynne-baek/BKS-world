from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def signup(request):
    pass

def login(request):
    pass

def logout(request):
    pass

def profile(request):
    return render(request, 'accounts/profile.html')

def follow(request):
    pass