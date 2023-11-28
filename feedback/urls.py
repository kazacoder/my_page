from django.urls import path
from .views import FeedBackView, DoneView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='feedback-index'),
    path('done', DoneView.as_view(), name='done'),
    path('feed_add', FeedBackView.as_view(), name='feedback-add'),
    path('<int:id_feed>', FeedBackView.as_view(), name='feedback-upd'),
]
