from horoscope.views import signs, sign_types, zodiac_dates
from datetime import datetime as dt
from django.test import TestCase


class Zodiac:

    def __init__(self, name, name_rus, description=None, sign_type=None, date_begin=None, date_end=None):
        self.name = name
        self.name_rus = name_rus
        self.description = description
        self.type = sign_type
        self.date_begin = date_begin
        self.date_end = date_end


def get_sign_type(sign):
    for sign_type in sign_types.items():
        if sign in sign_type[1]:
            return sign_type[0]


aries = Zodiac('Aries', signs['aries'][1], signs['aries'][0], get_sign_type('aries'), zodiac_dates['aries'][0],
               zodiac_dates['aries'][1])

print(aries.name)
print(aries.name_rus)
print(aries.description)
print(aries.type)
print(aries.date_begin)
print(aries.date_end)
