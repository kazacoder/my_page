from faker import Faker
from datetime import date

faker = Faker('ru_RU')

people = [
    {'name': faker.name(), 'age': date.today().year - int(faker.year()), 'phone': faker.phone_number()} for _ in range(15)
]
