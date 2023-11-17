from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('rectangle/<width>/<high>', views.get_rectangle_area ),
    path('square/<side>', views.get_square_area ),
    path('circle/<radius>', views.get_circle_area ),
]