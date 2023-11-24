from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, 'movie_app/movie.html')

