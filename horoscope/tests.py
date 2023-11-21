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
            self.assertIn(description[0], response.content.decode())

    def test_horoscope_redirect(self):
        for i, sign in enumerate(signs, 1):
            response = self.client.get(reverse('horoscope-name', args=(i, )))
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, reverse('horoscope-name', args=(sign, )))
