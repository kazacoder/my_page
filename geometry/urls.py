from django.urls import path
from . import views
urlpatterns = [
    path('calculate_geometry/', views.get_rectangle_area),
    path('', views.get_rectangle_area),
]