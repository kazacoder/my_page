from django.test import TestCase
from datetime import datetime
from .models import Student


class MovieModelTestCase(TestCase):

    @staticmethod
    def print_info(message):
        count = Student.objects.count()
        print(f"{message}: #all_students={count}")

    def setUp(self):
        print('-' * 20)
        self.print_info('Start setUp')
        self.petrov = Student.objects.create(first_name='Окакий', last_name='Петров', age=17, email='pqq@test.com')
        self.kim = Student.objects.create(first_name='Иван', last_name='Ким', age=18, email='kqq@test.com')
        Student.objects.create(first_name='Семен', last_name='Иванов', age=17, email='iqq@test.com')
        Student.objects.create(first_name='Нина', last_name='Сидорова', age=18, email='sqq@test.com')
        self.print_info('Finish setUp')

    def test_student_creation(self):
        # Проверка создания объекта Student
        self.print_info('Start test_movie_creation')
        self.assertEqual(self.kim.first_name, 'Иван')
        self.assertEqual(self.kim.last_name, 'Ким')
        self.assertEqual(self.kim.age, 18)
        self.assertEqual(self.kim.email, 'kqq@test.com')
        self.assertEqual(self.kim.created_at.strftime('%d-%m-%Y'), datetime.now().strftime('%d-%m-%Y'))
        self.print_info('Finish test_movie_creation')

    def test_student_get_all_records(self):
        # Проверка получения всех записей из бд
        self.print_info('Start test_student_get_all_records')
        movies = Student.objects.all()
        self.assertEqual(len(movies), 4)
        self.print_info('Finish test_student_get_all_records')

    def test_student_get_record(self):
        # Проверка получения записи из бд
        self.print_info('Start test_student_get_record')
        okaq = Student.objects.get(first_name='Окакий')
        self.assertEqual(okaq.last_name, 'Петров')
        self.print_info('Finish test_student_get_record')

    def test_student_adult(self):
        # Проверка метода is_adult()
        self.print_info('Start test_student_adult')
        test_stud = Student.objects.create(first_name='Name', last_name='Lname', age=18)
        test_stud2 = Student.objects.create(first_name='Name', last_name='Lname', age=17)
        self.assertEqual(test_stud.is_adult(), True)
        self.assertEqual(test_stud2.is_adult(), False)
        self.print_info('Finish test_student_adult')

    def test_student_full_name(self):
        # Проверка метода get_full_name()
        self.print_info('Start test_student_full_name')
        expected_str = 'Окакий Петров'
        self.assertEqual(self.petrov.get_full_name(), expected_str)
        self.print_info('Finish test_student_full_name')

    def test_student_date_default_value(self):
        # Проверка значения по умолчанию для created_at
        self.print_info('Start test_student_date_default_value')
        stud1 = Student.objects.create(first_name='Name', last_name='Lname', age=18)
        self.assertEqual(stud1.created_at.date(), datetime.now().date())
        self.print_info('Finish test_student_date_default_value')