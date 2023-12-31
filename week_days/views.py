from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from calendar import day_name
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

home = '<br><a href="/">home</a>'
back = '<br><a href="..">back</a>'


@login_required
def todo_week(request):
    return render(request, 'week_days/greeting.html')


@login_required
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


@login_required
def todo_weekday_by_number(request, weekday):
    if 0 < weekday < 8:
        redirect_url = reverse('todo-week', args=(day_name[weekday-1].lower(),))
        return HttpResponseRedirect(redirect_url)
    return HttpResponseNotFound(f'Неверный номер дня - {weekday}' + back + home)





