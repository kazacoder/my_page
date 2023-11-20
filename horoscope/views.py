from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.

home = '<br><a href="/">home</a>'
back = '<br><a href="..">back</a>'
signs = {
    'aries': ("<h1>♈</h1> [ɛəri:z] Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).", 'Овен'),
    'taurus': ("♉ ['tɔ:rəs] Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).", 'Телец'),
    'gemini': ("♊ ['dʒeminai] Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).", 'Близнецы'),
    'cancer': ("♋ ['kænsə(r)] Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).", 'Рак'),
    'leo': ("♌ ['li:əu] Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).", 'Лев'),
    'virgo': ("♍ ['vз:gəu] Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).", 'Дева'),
    'libra': ("♎ ['li:brə] Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).", 'Весы'),
    'scorpio': ("♏ ['skɔ:piəu] Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).", 'Скорпион'),
    'sagittarius': ("♐ [sædʒi'tɛəriəs] Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).", 'Стрелец'),
    'capricorn': ("♑ ['kæprikɔ:n] Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).", 'Козерог'),
    'aquarius': ("♒ [ə'kwɛəriəs] Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).", 'Водолей'),
    'pisces': ("♓ ['paisi:z] Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).", 'Рыбы'),
}


def index(request):
    return HttpResponse(f'''
                        <h1><a href="horoscope">Гороскоп</a></h1>
                        <h1><a href="todo_week">Список дел</a></h1>
                        <h1><a href="calculate_geometry">Геометрия</a></h1>
                        ''')


def horoscope(request):
    li_elem = ''
    for sign in signs.items():
        li_elem += f'<li><a href="{sign[0]}"><b>{sign[1][1]}</b> {" " + sign[0].title()}</a>'
    response = f'<ol>{li_elem}</ol><br><a href="/">home</a>'
    return HttpResponse(response)


def get_info_about_zodaic_sign(request, sign_zodiac: str):
    response = signs.get(sign_zodiac)
    if response:
        return HttpResponse(response[0] + back + home)
    return HttpResponseNotFound(f"такого знака - <b>{sign_zodiac}</b> - не существует" + back + home)


def get_info_about_zodaic_sign_by_number(request, sign_number: int):
    zodiacs = list(signs)
    if sign_number > len(zodiacs) or sign_number < 1:
        return HttpResponseNotFound(f'Неправильный порядковый номер знака зодиака {sign_number}')
    name_zodiac = zodiacs[sign_number - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac, ))
    return HttpResponseRedirect(redirect_url)
