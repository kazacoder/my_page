from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView

from .forms import AddMovieForm
from .models import Movie, Director, Actor


class MoviesList(ListView):
    model = Movie
    template_name = 'movie_app/movie.html'
    context_object_name = 'movies'

    def get_queryset(self):
        queryset = super().get_queryset()
        ordered_qs = queryset.order_by(F('year').asc(nulls_last=True))
        return ordered_qs


def directors(request):
    directors_list = Director.objects.all()
    return render(request, 'movie_app/directors.html', {"directors": directors_list})


def actors(request):
    actors_list = Actor.objects.all()
    return render(request, 'movie_app/actors.html', {"actors": actors_list})


class Index(TemplateView):
    template_name = 'movie_app/index.html'


class DetailMovie(DetailView):
    template_name = 'movie_app/detail_movie.html'
    model = Movie


class DetailDirector(DetailView):
    template_name = 'movie_app/detail_director.html'
    model = Director


class DetailActor(DetailView):
    template_name = 'movie_app/detail_actor.html'
    model = Actor


def add_movie(request):
    if request.method == 'POST':
        form = AddMovieForm(request.POST)
        if form.is_valid():
            # mov = Movie(
            #     name=form.cleaned_data['name'],
            #     rating=form.cleaned_data['rating'],
            #     year=form.cleaned_data['year'],
            #     budget=form.cleaned_data['budget'],
            #     director=Director.objects.get(id=form.cleaned_data['director']),
            # )
            form.save()
            return HttpResponseRedirect('/movie/movies')
    else:
        form = AddMovieForm()
    return render(request, 'movie_app/add_movie.html', context={'form': form})


# def movies(request):
#     movies_list = Movie.objects.order_by(F('year').asc(nulls_last=True))
#     return render(request, 'movie_app/movie.html', {"movies": movies_list})


# def details_director(request, id_director):
#     director = get_object_or_404(Director, id=id_director)
#     return render(request, 'movie_app/detail_director.html', {"director": director})


# def details_actor(request, id_actor):
#     actor = get_object_or_404(Actor, id=id_actor)
#     return render(request, 'movie_app/detail_actor.html', {"actor": actor})


# def details_movie(request, slug_movie: int):
#     movie = get_object_or_404(Movie, slug=slug_movie)
#     return render(request, 'movie_app/detail_movie.html', {"movie": movie})
