from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string
from datetime import datetime as dt


# Create your views here.

home = '<br><a href="/">home</a>'
back = '<br><a href="..">back</a>'
signs = {
    'aries': ("♈ [ɛəri:z] Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).", 'Овен'),
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

sign_types = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}

zodiac_dates = {
    "aries": (dt(2000, 3, 21), dt(2000, 4, 20)),
    "taurus": (dt(2000, 4, 21), dt(2000, 5, 21)),
    "gemini": (dt(2000, 5, 22), dt(2000, 6, 21)),
    "cancer": (dt(2000, 6, 22), dt(2000, 7, 22)),
    "leo": (dt(2000, 7, 23), dt(2000, 8, 21)),
    "virgo": (dt(2000, 8, 22), dt(2000, 9, 23)),
    "libra": (dt(2000, 9, 24), dt(2000, 10, 23)),
    "scorpio": (dt(2000, 10, 24), dt(2000, 11, 22)),
    "sagittarius": (dt(2000, 11, 23), dt(2000, 12, 22)),
    "capricorn": (dt(1999, 12, 23), dt(2000, 1, 20)),
    "aquarius": (dt(2000, 1, 21), dt(2000, 2, 19)),
    "pisces": (dt(2000, 2, 20), dt(2000, 3, 20))
}


def get_sign_http_list(sign_list=signs):
    li_elem = ''
    for sign in signs.items():
        if sign[0] in sign_list:
            reference = reverse('horoscope-name', args=(sign[0], ))
            li_elem += f'<li><a href="{reference}"><b>{sign[1][1]}</b> {" " + sign[0].title()}</a>'
    return li_elem


def index(request):
    return HttpResponse(render_to_string('root/index.html'))


def sign_type(request):
    li_elem = ''
    for type_sign in sign_types:
        li_elem += f'<li><a href="{type_sign}/">{type_sign.title()}</a>'
    response = f'<ul>{li_elem}</ul>'
    return HttpResponse(response + back + home)


def current_sign_type_list(request, type_of_sign):
    if type_of_sign in sign_types:
        li_elem = get_sign_http_list(sign_types[type_of_sign])
        response = f'<h1>{type_of_sign.title()}</h1><ul>{li_elem}</ul><br><br>'
        return HttpResponse(response + back + home)
    return HttpResponseNotFound(f"Такой стихии - <b>{type_of_sign}</b> - не существует" + back + home)


def horoscope(request):
    li_elem = get_sign_http_list()
    response = f'<ol>{li_elem}</ol><br><br><a href="type/">Знаки по стихии</a><br><a href="/">home</a>'
    return HttpResponse(response)


def get_info_about_zodiac_sign(request, sign_zodiac: str):
    description = signs.get(sign_zodiac)
    if description:
        response = render(request, 'horoscope/info_zodiac.html',
                          {'description': description[0], 'sign': sign_zodiac.title()})
        return response
    return HttpResponseNotFound(f"такого знака - <b>{sign_zodiac}</b> - не существует" + back + home)


def get_info_about_zodiac_sign_by_number(request, sign_number: int):
    zodiacs = list(signs)
    if sign_number > len(zodiacs) or sign_number < 1:
        return HttpResponseNotFound(f'Неправильный порядковый номер знака зодиака {sign_number}')
    name_zodiac = zodiacs[sign_number - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac, ))
    return HttpResponseRedirect(redirect_url)


def get_info_by_date(request, month, day):
    sign_by_date = get_sign_by_date(month, day)
    if sign_by_date[1]:
        return HttpResponseNotFound(f'<h1>{sign_by_date[0]}</h1>')
    redirect_url = reverse('horoscope-name', args=(sign_by_date[0],))
    return HttpResponseRedirect(redirect_url)


def get_sign_by_date(month, day):
    try:
        dt(2000, month, day)
        filtered_month = filter(lambda x: (x[1][0].month == month and x[1][0].day <= day)
                                          or (x[1][1].month == month and x[1][0].day >= day),
                                zodiac_dates.items())
        response = tuple(filtered_month)[0][0]
        error = False
    except ValueError as e:
        if str(e) == 'day is out of range for month':
            response = 'Неверный номер дня'
        elif str(e) == 'month must be in 1..12':
            response = 'месяц должен быть в диапазоне 1..12'
        else:
            response = str(e)
        error = True
    return response, error


def get_my_date_converters(request, date):
    redirect_url = reverse('horoscope-name', args=(get_sign_by_date(date.month, date.day)[0],))
    return HttpResponseRedirect(redirect_url)


def get_yyyy_converters(request, sign_zodiac):
    return HttpResponse(f'Год {sign_zodiac}')


def get_my_float_converters(request, sign_zodiac):
    return HttpResponse(f'Флоат {sign_zodiac}')


def get_list_from_str(request, value):
    return HttpResponse(str(value))


def value_to_upper(request, value):
    return HttpResponse(value)