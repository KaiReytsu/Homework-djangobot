from re import template
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth import authenticate as auth
from django.contrib.auth import login
from django.views import generic
from .forms import LoginFrom
from .models import Book

class BooksList(generic.ListView):
    model = Book
    template_name = 'polls/succes_reg.html'


def index(request):
    return render(request, 'polls/index.html')

def dtnow(request):
    datenow = datetime.now()
    return render(request,'polls/dtnow.html', {'mydate': datenow})

def startpage(request):
    return render(request, 'polls/startpage.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginFrom(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = auth(username = cd['логин'], password = cd['пароль'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('books')
                else:
                    return render(request, 'polls/fail_reg.html')
            else:
                return render(request, 'polls/fail_reg.html')
    else:
        form = LoginFrom()
    return render(request, 'polls/login.html', {'form': form})


   