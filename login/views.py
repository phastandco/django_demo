from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('Home Page')


def login(request):
    return render(request, 'login/login.html')


def register(request):
    return render(request, 'login/register.html')


def connect(request):
    return HttpResponse('Connect Page')

