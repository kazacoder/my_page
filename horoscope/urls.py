from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyFloatConverter, 'my_float')
register_converter(converters.MyDateConverter, 'my_date')

urlpatterns = [
    path('type/', views.sign_type),
    path('type/<str:type_of_sign>/', views.current_sign_type_list),
    path('<my_date:date>/', views.get_my_date_converters),
    path('<yyyy:sign_zodiac>/', views.get_yyyy_converters),
    path('<int:sign_number>/', views.get_info_about_zodiac_sign_by_number),
    path('<my_float:sign_zodiac>/', views.get_my_float_converters),
    path('<str:sign_zodiac>/', views.get_info_about_zodiac_sign, name='horoscope-name'),
    path('', views.horoscope),
    path('<int:month>/<int:day>/', views.get_info_by_date),
]
