from django.urls import path
from . import views

urlpatterns = [
    path('lessons/', views.index, name='lessons'),
    path('marks/', views.marks, name='marks')
    #path('<int:lesson_id>/', views.save_marks, name='mark')
]