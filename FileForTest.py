from horoscope.views import signs
from django.test import TestCase

for sign, description in signs.items():

    print(sign, description[0])