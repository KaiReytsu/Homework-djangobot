from django.urls import path
# from django.conf.urls.static import static
# from django.conf import settings

from . import views

urlpatterns = [
    path('startpage/', views.startpage, name='startpage'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.UserLogout.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(), name='registration'),
    path('books/', views.book_view, name='books'),
    path('start/', views.index, name='index'),
    path('time/', views.dtnow, name='dtnow'),
    path('welcomepage/', views.welcome_view ,name='welcome')
] 
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)