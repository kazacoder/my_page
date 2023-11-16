from django.urls import path

from . import views

urlpatterns = [
    path('<weekday>/', views.todo_weekday),
    path('', views.todo_week),
]