from django.shortcuts import render
from .forms import FeedbackForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import Feedback


def feed_add(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # feed = Feedback(
            #     name=form.cleaned_data['name'],
            #     surname=form.cleaned_data['surname'],
            #     feedback=form.cleaned_data['feedback'],
            #     rating=form.cleaned_data['rating']
            # )
            form.save()
            return HttpResponseRedirect('done')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback.html', context={'form': form})


def index(request):
    context = {'feeds': Feedback.objects.all()}
    return render(request, 'feedback/feedback_index.html', context=context)


def done(request):
    return render(request, 'feedback/done.html')


def feed_upd(request, id_feed):
    feed = Feedback.objects.get(id=id_feed)
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/feedback')
    else:
        form = FeedbackForm(instance=feed)
    return render(request, 'feedback/feedback.html', context={'form': form, 'upd': True})
