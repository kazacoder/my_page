from django.urls import path

from . import views

urlpatterns = [
    path('<sign_zodiac>/', views.get_info_about_zodaic_sign),
    # path('aries/', views.aries),
    # path('taurus/', views.taurus),
    # path('gemini/', views.gemini),
    # path('cancer/', views.cancer),
    # path('leo/', views.leo),
    # path('virgo/', views.virgo),
    # path('libra/', views.libra),
    # path('scorpio/', views.scorpio),
    # path('sagittarius/', views.sagittarius),
    # path('capricorn/', views.capricorn),
    # path('aquarius/', views.aquarius),
    # path('pisces/', views.pisces),
    path('', views.horoscope),
]