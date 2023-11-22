from faker import Faker
from datetime import  date

people1 = [
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

faker = Faker('ru_RU')

people = [
    {'name': faker.name(), 'age': date.today().year - int(faker.year()), 'phone': faker.phone_number()} for _ in range(15)
]

print(*people)
