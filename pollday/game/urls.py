from django.urls import path
from . import views

urlpatterns = [
    path('gameplay/', views.game_view, name='gameplay'),
    path('statistics/', views.game_statistics, name = 'statistics'),
]