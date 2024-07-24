from django.shortcuts import render,redirect
from.import forms
from django.contrib.auth import authenticate,login, logout
# Create your views here.
def index(request):
  return render(request, 'log/index.html')

def login(request):
  # print(request.__dict__.items())
  for i in request.__dict__.items():
    print(i)
  # for key, value in request.__dict__.items():
  #     print(f"{key}: {value}")
  return render(request,'log/login.html')
