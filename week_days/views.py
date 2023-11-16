from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

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
    return HttpResponse(todo_days.get(weekday, 'Не правильный день недели') + back + home)





