from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from .forms import FeedbackForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import Feedback
from django.views import View


class FeedBackView(LoginRequiredMixin, View):
    @staticmethod
    def get(request, id_feed=None):
        if id_feed:
            form = FeedbackForm(instance=Feedback.objects.get(id=id_feed))
            upd = True
        else:
            form = FeedbackForm()
            upd = False
        return render(request, 'feedback/feedback.html', context={'form': form, 'upd': upd})

    @staticmethod
    def post(request, id_feed=None):
        if id_feed:
            feed = Feedback.objects.get(id=id_feed)
            form = FeedbackForm(request.POST, instance=feed)
            upd = True
        else:
            form = FeedbackForm(request.POST)
            upd = ''
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('done' + f'?upd={upd}')
        return render(request, 'feedback/feedback.html', context={'form': form, 'upd': upd})


class IndexView(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        return render(request, 'feedback/feedback_index.html', {'feeds': Feedback.objects.all()})


class DoneView(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        upd = request.GET.get('upd')
        return render(request, 'feedback/done.html', {'upd': upd})


# def feed_add(request):
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             # feed = Feedback(
#             #     name=form.cleaned_data['name'],
#             #     surname=form.cleaned_data['surname'],
#             #     feedback=form.cleaned_data['feedback'],
#             #     rating=form.cleaned_data['rating']
#             # )
#             form.save()
#             return HttpResponseRedirect('done')
#     else:
#         form = FeedbackForm()
#     return render(request, 'feedback/feedback.html', context={'form': form})
#
#
# def feed_upd(request, id_feed):
#     feed = Feedback.objects.get(id=id_feed)
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST, instance=feed)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/feedback')
#     else:
#         form = FeedbackForm(instance=feed)
#     return render(request, 'feedback/feedback.html', context={'form': form, 'upd': True})
