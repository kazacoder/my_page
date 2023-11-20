from django.test import TestCase

# Create your tests here.

class TestHoroscope(TestCase):

    def test_horoscope_root(self):
        response = self.client.get('/horoscope/')
        self.assertEqual(response.status_code, 200)

    def test_horoscope_libra(self):
        response = self.client.get('/horoscope/libra/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Весы - седьмой знак зодиака, планета Венера', response.content.decode())

    def test_horoscope_libra_redirect(self):
        response = self.client.get('/horoscope/7/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/horoscope/libra/')
