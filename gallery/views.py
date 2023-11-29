import os
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import GalleryUploadForm
from django.views.generic import CreateView, ListView

from .models import Gallery


def get_files_list(directory):
    return os.listdir(directory)


class GalleryView(CreateView):
    model = Gallery
    form_class = GalleryUploadForm
    template_name = 'gallery/load_file.html'
    success_url = 'load_file'


class IndexView(ListView):
    model = Gallery
    template_name = 'gallery/gallery_index.html'
    context_object_name = 'files'


# class GalleryView(View):
#     def get(self, request):
#         form = GalleryUploadForm
#         return render(request, 'gallery/load_file.html', {'form': form})
#
#     def post(self, request):
#         form = GalleryUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_file = Gallery(file=form.cleaned_data['file'])
#             new_file.save()
#         return render(request, 'gallery/load_file.html', {'form': form})

    # def post(self, request):
    #     form = GalleryUploadForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         storage_file(request.FILES.get('file'))
    #         return HttpResponseRedirect('load_file')
    #     return render(request, 'gallery/load_file.html', {'form': form})


# def storage_file(file):
#     with open(f'gallery/files/{file.name}', 'wb+') as new_file:
#         for chunk in file.chunks():
#             new_file.write(chunk)
#     pass



