from horoscope.views import signs, sign_types, zodiac_dates
from datetime import datetime as dt
from django.test import TestCase
from faker import Faker


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



print([Faker("ru_RU").name() for _ in range(10)])

people = [
    'Цветков Алексей Якубович',
    'Ювеналий Феликсович Лазарев',
    'Овчинников Измаил Эдуардович',
    'Анастасия Антоновна Бобылева',
    'Майя Никифоровна Михайлова',
    'Радован Владиленович Колобов',
    'Мухина Виктория Захаровна',
    'Мокей Захарьевич Виноградов',
    'Крылова Наталья Романовна',
    'Милан Викторович Кабанов'
]