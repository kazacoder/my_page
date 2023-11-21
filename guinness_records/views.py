from django.http import HttpResponse
from django.shortcuts import render
from .records_list import records_list
# Create your views here.


def index(request):
    data = {'record_list': [record for record in records_list]}
    return render(request, 'guinness_records/record_list.html', data)


def record(request, record):
    data = {'title': record, 'description': records_list[record]['description']}
    return render(request, 'guinness_records/guinness_record.html', data)