from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse('''
                        <h1><a href="horoscope">Гороскоп</a></h1>
                        <h1><a href="todo_week">Список дел</a></h1>
                        <h1><a href="calculate_geometry">Геометрия</a></h1>
                        ''')


def horoscope(request):
    return HttpResponse('''
                        <h1>Гороскоп</h1>
                        <ol>
                        <li><a href="aries">Овен</a>
                        <li><a href="taurus">Телец</a>
                        <li><a href="gemini">Близнецы</a>
                        <li><a href="cancer">Рак</a>
                        <li><a href="leo">Лев</a>
                        <li><a href="virgo">Дева</a>
                        <li><a href="libra">Весы</a>
                        <li><a href="scorpio">Скорпион</a>
                        <li><a href="sagittarius">Стрелец</a>
                        <li><a href="capricorn">Козегор</a>
                        <li><a href="aquarius">Володей</a>
                        <li><a href="pisces">Рыбы</a>
                        </ol>
                        <br>
                        <a href="/">home</a>
                        ''')


home = '<br><a href="/">home</a>'
back = '<br><a href="..">back</a>'
signs = {
    'aries': "<h1>♈</h1> [ɛəri:z] Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    'taurus': "♉ ['tɔ:rəs] Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    'gemini': "♊ ['dʒeminai] Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    'cancer': "♋ ['kænsə(r)] Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    'leo': "♌ ['li:əu] Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
    'virgo': "♍ ['vз:gəu] Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    'libra': "♎ ['li:brə] Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    'scorpio': "♏ ['skɔ:piəu] Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
    'sagittarius': "♐ [sædʒi'tɛəriəs] Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    'capricorn': "♑ ['kæprikɔ:n] Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    'aquarius': "♒ [ə'kwɛəriəs] Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
    'pisces': "♓ ['paisi:z] Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).",
}


def get_info_about_zodaic_sign(request, sign_zodiac: str):
    response = signs.get(sign_zodiac)
    if response:
        return HttpResponse(response + back + home)
    return HttpResponseNotFound(f"такого знака - <b>{sign_zodiac}</b> - не существует" + back + home)


def get_info_about_zodaic_sign_by_number(request, sign_zodiac: str):
    return HttpResponse(f'number {sign_zodiac}')
