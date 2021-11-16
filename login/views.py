from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'login/index.html')


def login(request):
    return render(request, 'login/login.html')


def register(request):
    return render(request, 'login/register.html')


def admin(request):
    return render(request, 'login/admin.html')


def connected(request):
    return render(request, 'login/connected.html')