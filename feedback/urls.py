from django.urls import path
from .views import FeedBackView, DoneView, IndexView, DetailFeedBack, FeedBackViewUpd, FeedBackViewDel

urlpatterns = [
    path('', IndexView.as_view(), name='feedback-index'),
    path('done', DoneView.as_view(), name='done'),
    path('feed_add', FeedBackView.as_view(), name='feedback-add'),
    path('<int:pk>', DetailFeedBack.as_view(), name='detail-feedback'),
    path('upd/<int:pk>', FeedBackViewUpd.as_view(), name='feedback-upd'),
    path('del/<int:pk>', FeedBackViewDel.as_view(), name='feedback-del'),
]
