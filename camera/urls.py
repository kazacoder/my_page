from django.urls import path, register_converter
from camera.views import *


urlpatterns = [
    path('go/', CameraGo.as_view(), name='camera-go'),

]
