from django.urls import path
from .views import index, done, feed_add, feed_upd

urlpatterns = [
    path('', index, name='feedback-index'),
    path('done', done, name='done'),
    path('feed_add', feed_add, name='feedback-add'),
    path('<int:id_feed>', feed_upd, name='feedback-upd'),
]
