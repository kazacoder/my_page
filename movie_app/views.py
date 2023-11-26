from django.db.models import F
from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Actor


def movies(request):
    movies_list = Movie.objects.order_by(F('year').asc(nulls_last=True))
    return render(request, 'movie_app/movie.html', {"movies": movies_list})


def directors(request):
    directors_list = Director.objects.all()
    return render(request, 'movie_app/directors.html', {"directors": directors_list})


def actors(request):
    actors_list = Actor.objects.all()
    return render(request, 'movie_app/actors.html', {"actors": actors_list})


def index(request):
    return render(request, 'movie_app/index.html')


def details_movie(request, slug_movie: int):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/detail_movie.html', {"movie": movie})


def details_director(request, id_director):
    director = get_object_or_404(Director, id=id_director)
    return render(request, 'movie_app/detail_director.html', {"director": director})


def details_actor(request, id_actor):
    actor = get_object_or_404(Actor, id=id_actor)
    return render(request, 'movie_app/detail_actor.html', {"actor": actor})
