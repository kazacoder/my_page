from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from .forms import FeedbackForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import Feedback
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404


class FeedBackViewDel(LoginRequiredMixin, DeleteView):
    model = Feedback
    success_url = reverse_lazy('feedback-index')
    template_name = 'feedback/delete.html'


class FeedBackView(LoginRequiredMixin, CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = reverse_lazy("done")


class FeedBackViewUpd(LoginRequiredMixin, UpdateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    # success_url = reverse_lazy('done')

    def get(self, request, *args, **kwargs):
        context = super().get(self, request, *args, **kwargs)
        context.context_data['upd'] = True
        return context

    def get_success_url(self):
        return reverse_lazy('done') + '?upd=True'


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'feedback/feedback_index.html'
    model = Feedback
    context_object_name = 'feeds'


class DetailFeedBack(LoginRequiredMixin, DetailView):
    template_name = 'feedback/detail_feedback.html'
    model = Feedback
    context_object_name = 'feed'


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


# class IndexView(LoginRequiredMixin, TemplateView):
#     template_name = 'feedback/feedback_index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['feeds'] = Feedback.objects.all()
#         return context

# class FeedBackView(LoginRequiredMixin, View):
#     @staticmethod
#     def get(request, id_feed=None):
#         if id_feed:
#             form = FeedbackForm(instance=Feedback.objects.get(id=id_feed))
#             upd = True
#         else:
#             form = FeedbackForm()
#             upd = False
#         return render(request, 'feedback/feedback.html', context={'form': form, 'upd': upd})
#
#     @staticmethod
#     def post(request, id_feed=None):
#         if id_feed:
#             feed = Feedback.objects.get(id=id_feed)
#             form = FeedbackForm(request.POST, instance=feed)
#             upd = True
#         else:
#             form = FeedbackForm(request.POST)
#             upd = ''
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('done') + f'?upd={upd}')
#         return render(request, 'feedback/feedback.html', context={'form': form, 'upd': upd})


# class FeedBackView(LoginRequiredMixin, FormView):
#     form_class = FeedbackForm
#     template_name = 'feedback/feedback.html'
#     success_url = reverse_lazy('done')
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
