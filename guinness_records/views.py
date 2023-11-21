from django.http import HttpResponse
from django.shortcuts import render
from .records_list import records_list
# Create your views here.


def index(request):
    data = {'record_list': [(i, record['title']) for i, record in enumerate(records_list)]}
    return render(request, 'guinness_records/record_list.html', data)


def record(request, record):
    data = records_list[int(record)]
    context = {'title': data['title'], 'description': data['description']}
    return render(request, 'guinness_records/guinness_record.html', context)