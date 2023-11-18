from django.http import HttpResponse, HttpResponseRedirect
from math import pi
from django.shortcuts import render


# Create your views here.

def get_rectangle_area(request, width, high):
    return HttpResponse(f"Площадь прямоугольника размером {width} х {high} = {int(width) * int(high)}")


def get_square_area(request, side):
    return HttpResponse(f"Площадь квадрата со стороной {side} = {int(side) ** 2}")


def get_circle_area (request, radius):
    return HttpResponse(f"Площадь круга с радиусом {radius} = {round(int(radius) ** 2 * pi, 2)}")


def index(request):
    return HttpResponse(f"Геометрия")


def redirect_to_route(request, shape=None, a=None, b=None):
    redirect_dict = {
                        'get_rectangle_area': f'/calculate_geometry/rectangle/{a}/{b}',
                        'get_circle_area': f'/calculate_geometry/circle/{a}',
                        'get_square_area': f'/calculate_geometry/square/{a}'
                    }
    if shape in redirect_dict.keys():
        return HttpResponseRedirect(redirect_dict[shape])
    return HttpResponse(f'{shape}')