from django.test import TestCase
from django.urls import reverse
from .views import signs

# Create your tests here.


class TestHoroscope(TestCase):

    def test_horoscope_root(self):
        response = self.client.get('/horoscope/')
        self.assertEqual(response.status_code, 200)

    def test_horoscope_libra(self):
        response = self.client.get('/horoscope/libra/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Весы - седьмой знак зодиака, планета Венера', response.content.decode())

    def test_horoscope_signs(self):
        for sign, description in signs.items():
            response = self.client.get(reverse('horoscope-name', args=(sign, )))
            self.assertEqual(response.status_code, 200)
            self.assertIn(' '.join(description[0].split()[2:]), response.content.decode())  # убираем из описания спец
                                                                                            # символы, т.к. при
                                                                                            # декодировании из html
                                                                                            # они меняются

    def test_horoscope_redirect(self):
        for i, sign in enumerate(signs, 1):
            response = self.client.get(reverse('horoscope-name', args=(i, )))
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, reverse('horoscope-name', args=(sign, )))


