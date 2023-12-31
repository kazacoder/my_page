from django.urls import path

from . import views

urlpatterns = [
    path('<int:weekday>/', views.todo_weekday_by_number),
    path('<str:weekday>/', views.todo_weekday, name='todo-week'),
    path('', views.todo_week),
]