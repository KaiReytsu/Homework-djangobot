from django.urls import reverse_lazy
from django.shortcuts import render
from datetime import datetime
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SignUpForm
from .models import Book, Author, Genre

class SignUp(SuccessMessageMixin, CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'polls/registration.html'

class UserLogin(LoginView):
    template_name = 'polls/login.html'

class UserLogout(LogoutView):
    template_name = 'polls/logout.html'

# class BooksList(LoginRequiredMixin, ListView):
#     model = Book
#     template_name = 'polls/books.html'

@login_required
def book_view(request):
    book = Book.objects.all()
    return render(request, 'polls/books.html', {"book":book})

@login_required
def welcome_view(request):
    return render(request, 'polls/userpage.html')

def index(request):
    return render(request, 'polls/index.html')

def dtnow(request):
    datenow = datetime.now()
    return render(request,'polls/dtnow.html', {'mydate': datenow})

def startpage(request):
    return render(request, 'polls/startpage.html')


   