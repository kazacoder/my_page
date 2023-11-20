from django.urls import path

from . import views

urlpatterns = [
    path('<int:sign_number>/', views.get_info_about_zodaic_sign_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_zodaic_sign, name='horoscope-name'),
    path('', views.horoscope),
]
