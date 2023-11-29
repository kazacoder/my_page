from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('movies', views.MoviesList.as_view(), name='movies'),
    path('movies/add_movie', views.add_movie, name='add-movie'),
    path('directiors', views.directors, name='directors'),
    path('actiors', views.actors, name='actors'),
    path("movies/<slug>", views.DetailMovie.as_view(), name='movie'),
    path("directiors/<pk>", views.DetailDirector.as_view(), name='director'),
    path("actiors/<pk>", views.DetailActor.as_view(), name='actor'),
]
