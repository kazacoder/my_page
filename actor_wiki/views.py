from django.http import HttpResponse
from django.shortcuts import render
from .actors_dict import reeves


# Create your views here.


def index(request):
    return render(request, 'actor_wiki/actor_wiki_idx.html')


def actor_info(request):
    data = {
        'year_born': reeves.year_born,
        'city_born': reeves.city_born,
        'movie_name': reeves.movie_name,
    }
    return render(request, 'actor_wiki/actor_info.html', data)