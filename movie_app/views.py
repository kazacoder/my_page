from django.shortcuts import render, get_object_or_404
from .models import Movie



def index(request):
    movies = Movie.objects.all()
    return render(request, 'movie_app/movie.html', {"movies": movies})


def details_movie(request, slug_movie: int):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/detail_movie.html', {"movie": movie})
