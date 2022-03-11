from cmath import log
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import UserCreationForm


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect('/home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('/home')
    return render(request, "index.html")

@login_required(login_url='/')
def home(request):
    return render(request ,"home.html")


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/home')
    return redirect('/')



@login_required(login_url='/')
def logoutPage(request):
    logout(request)
    return redirect('/')

def registration(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        forms = UserCreationForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(username=username, password=password)
        if not (user is not None):
            if forms.is_valid():
                forms.save()
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/home')
    else:
        forms = UserCreationForm()
    return render(request , "register.html", {'form': forms})
    
@login_required(login_url='/')
def myorder(request):
    return render(request,"myorder.html")

@login_required(login_url='/')
def sustainable(request):
    return render(request,"sustainable.html")

def contactus(request):
    return render(request,"contactus.html")

@login_required(login_url='/')
def distribution(request):
    return render(request,"distribution.html")