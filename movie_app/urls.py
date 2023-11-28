from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('movies', views.MoviesList.as_view(), name='movies'),
    path('movies/add_movie', views.add_movie, name='add-movie'),
    path('directiors', views.directors, name='directors'),
    path('actiors', views.actors, name='actors'),
    path("movies/<slug:slug_movie>", views.details_movie, name='movie'),
    path("directiors/<id_director>", views.details_director, name='director'),
    path("actiors/<id_actor>", views.details_actor, name='actor'),
]
