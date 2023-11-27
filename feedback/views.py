from django.shortcuts import render
from .forms import FeedbackForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import Feedback


def index(request):
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


def done(request):
    return render(request, 'feedback/done.html')
