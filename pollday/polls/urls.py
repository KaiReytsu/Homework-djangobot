from django.urls import path
from . import views

urlpatterns = [
    path('startpage/', views.startpage, name='startpage'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.UserLogout.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(), name='registration'),
    path('books/', views.book_view, name='books'),
    path('book/<int:pk>/', views.book_detail_view, name='book-detail'),
    path('start/', views.index, name='index'),
    path('time/', views.dtnow, name='dtnow'),
    path('welcomepage/', views.welcome_view ,name='welcome')
]