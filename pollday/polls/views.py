# Добавить в возвращаемую 
# в браузер строку текущую дату и время.
# Выполняя тест, игнорировать дату и время,
# т.е. выдавать результат "Ок", если всё,
# кроме даты и времени совпадает с
# записанным в тесте. 
# Клиент разместить в функции setup
# Собрать отчет в виде html
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from datetime import datetime

def index(request):
    return render(request, 'polls/index.html')

def dtnow(request):
    datenow = datetime.now()
    return render(request,'polls/dtnow.html', {'mydate': datenow})

def startpage(request):
    return render(request, 'polls/startpage.html')