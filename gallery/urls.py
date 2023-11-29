from django.urls import path
from . import views
urlpatterns = [
    path('load_file', views.GalleryView.as_view()),
    path('', views.IndexView.as_view(), name='gallery'),
]