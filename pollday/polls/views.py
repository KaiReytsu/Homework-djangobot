from pyexpat import model
from django.urls import reverse_lazy
from re import template
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth import authenticate as auth
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from .forms import SignUpForm
from .models import Book

class SignUp(SuccessMessageMixin, CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'polls/registration.html'

class UserLogin(LoginView):
    template_name = 'polls/login.html'

class UserLogout(LogoutView):
    template_name = 'polls/logout.html'

class BooksList(ListView):
    model = Book
    template_name = 'polls/books.html'

def welcome_view(request):
    return render(request, 'polls/userpage.html')

def index(request):
    return render(request, 'polls/index.html')

def dtnow(request):
    datenow = datetime.now()
    return render(request,'polls/dtnow.html', {'mydate': datenow})

def startpage(request):
    return render(request, 'polls/startpage.html')


   