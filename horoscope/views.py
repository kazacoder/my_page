from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime as dt
from .zodiac_sings import signs, sign_types, zodiac_dates


# Create your views here.

home = '<br><a href="/">home</a>'
back = '<br><a href="..">back</a>'


def get_sign_http_list(sign_list=signs):
    li_elem = ''
    for sign in signs.items():
        if sign[0] in sign_list:
            reference = reverse('horoscope-name', args=(sign[0], ))
            li_elem += f'<li><a href="{reference}"><b>{sign[1][1]}</b> {" " + sign[0].title()}</a>'
    return li_elem


def index(request):
    return render(request, 'root/index.html')


def sign_type(request):
    context = {'sign_types': sign_types.keys()}
    return render(request, 'horoscope/horoscope_types.html', context)


def current_sign_type_list(request, type_of_sign):
    if type_of_sign in sign_types:
        li_elem = get_sign_http_list(sign_types[type_of_sign])
        response = f'<h1>{type_of_sign.title()}</h1><ul>{li_elem}</ul><br><br>'
        return HttpResponse(response + back + home)
    return HttpResponseNotFound(f"Такой стихии - <b>{type_of_sign}</b> - не существует" + back + home)


def horoscope(request):
    context = {'signs_list': [(k, v[1]) for k, v in signs.items()]}
    return render(request, 'horoscope/horoscope_index.html', context)


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
    return HttpResponse(f'вещественное число {sign_zodiac}')


def get_list_from_str(request, value):
    return HttpResponse(str(value))


def value_to_upper(request, value):
    return HttpResponse(value)