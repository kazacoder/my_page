from django.urls import path
from .views import index, done

urlpatterns = [
    path('', index, name='feedback-index'),
    path('done', done, name='done'),
]
