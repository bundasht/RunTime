from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from . import models


# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    return render(request, 'register.html')
def login(request):
    return render(request, 'login.html')


class UserInfoView(generic.CreateView):
    fields = '__all__'
    model = models.UserInfo