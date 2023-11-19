from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from calendar import day_name
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

home = '<br><a href="/">home</a>'
back = '<br><a href="..">back</a>'

def todo_week(request):
    return HttpResponse('''
                        <h1>Список дел</h1>
                        <ol>
                        <li><a href="monday">Понедельник</a>
                        <li><a href="tuesday">Вторник</a>
                        <li><a href="wednesday">Среда</a>
                        <li><a href="thursday">Четверг</a>
                        <li><a href="friday">Пятница</a>
                        <li><a href="saturday">Суббота</a>
                        <li><a href="sunday">Воскресенье</a>
                        </ol>
                        ''' + home)


def todo_weekday(request, weekday):
    todo_days = {
        'monday': '''<h1>Список дел на понедельник</h1>
                  <ol>
                  <li> Дыхательные практики
                  <li> Сурья Намаскар
                  <li> Медитация
                  <li> Работа в офисе
                  <li> Упражнения для падмасаны
                  </ol>
                  ''',
        'tuesday': 'Список дел на вторник',
        'wednesday': 'Список дел на среду',
        'thursday': 'Список дел на четверг',
        'friday': 'Список дел на пятницу',
        'saturday': 'Список дел на субботу',
        'sunday': 'Список дел на воскресенье'
    }
    response = todo_days.get(weekday)
    if response:
        return HttpResponse(response + back + home)
    return HttpResponseNotFound(f'Не правильный день недели {weekday}' + back + home)


def todo_weekday_by_number(request, weekday):
    if 0 < weekday < 8:
        redirect_url = reverse('todo-week', args=(day_name[weekday-1].lower(),))
        return HttpResponseRedirect(redirect_url)
    return HttpResponseNotFound(f'Неверный номер дня - {weekday}' + back + home)





