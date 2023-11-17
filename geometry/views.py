from django.http import HttpResponse
from math import pi
from django.shortcuts import render


# Create your views here.

def get_rectangle_area(request, width, high):
    return HttpResponse(f"Площадь прямоугольника размером {width} х {high} = {int(width) * int(high)}")


def get_square_area(request, side):
    return HttpResponse(f"Площадь квадрата со стороной {side} = {int(side) ** 2}")


def get_circle_area (request, radius):
    return HttpResponse(f"Площадь квадрата с радиусом {radius} = {round(int(radius) ** 2 * pi, 2)}")


def index(request):
    return HttpResponse(f"Геометрия")
