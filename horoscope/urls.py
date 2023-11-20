from django.urls import path

from . import views

urlpatterns = [
    path('type/', views.sign_type),
    path('type/<str:type_of_sign>/', views.current_sign_type_list),
    path('<int:sign_number>/', views.get_info_about_zodiac_sign_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_zodiac_sign, name='horoscope-name'),
    path('', views.horoscope),
    path('<int:month>/<int:day>/', views.get_info_by_date),
]
