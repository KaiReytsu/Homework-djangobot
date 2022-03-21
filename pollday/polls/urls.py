from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.startpage, name='startpage'),
    path('start/', views.index, name='index'),
    path('time/', views.dtnow, name='dtnow')
]