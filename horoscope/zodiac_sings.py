from datetime import datetime as dt

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
