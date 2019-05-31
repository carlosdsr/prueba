from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView, TemplateView
from usuario.models import User
from .forms import InicioSesionForm
from django.contrib.auth.views import LoginView


def home(request):
    return render(request, 'home/inicioSesion.html')


def dashboard(request):
    return render(request, 'home/dashboard.html')

def loginview(request):
     if request.method == 'POST':
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            return redirect('dashboardjvc')

     else:
            form = AuthenticationForm()
     return render(request,'home/inicioSesion.html',{'form':form})