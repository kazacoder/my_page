from dataclasses import dataclass


@dataclass
class Actor:
    year_born: int
    city_born: str
    movie_name: str


reeves = Actor(1964, 'Бейрут', 'На гребне волны')