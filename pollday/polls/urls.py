from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.startpage, name='startpage'),
    path('login/', views.user_login, name='login'),
    path('boos/',views.BooksList.as_view() , name='books'),
    path('start/', views.index, name='index'),
    path('time/', views.dtnow, name='dtnow')
]