from django.shortcuts import render
from .people import people as people_list
# Create your views here.


def index(request):
    return render(request, 'app_for_tests/index.html')


def people(request):
    return render(request, 'app_for_tests/people.html', {'people': people_list})


def gamers(request):
    return render(request, 'app_for_tests/gamers.html')
