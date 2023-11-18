from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('rectangle/<int:width>/<int:high>', views.get_rectangle_area ),
    path('square/<int:side>', views.get_square_area ),
    path('circle/<int:radius>', views.get_circle_area ),
    path('<shape>/<int:a>/<int:b>', views.redirect_to_route),
    path('<shape>/<int:a>', views.redirect_to_route),

]