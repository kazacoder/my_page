from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from pytils.translit import slugify

# Create your models here.



class Movie(models.Model):
    EUR = "EUR"
    USD = "USD"
    RUR = "RUR"
    CURRENCY_CHOICES = [
        (EUR, "Euro"),
        (USD, "US Dollar"),
        (RUR, "Ruble"),
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1_000_000, validators=[MinValueValidator(1)])
    slug = models.SlugField(default='', null=False, db_index=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=USD)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('movie', args=(self.slug, ))

    def __str__(self):
        return f'{self.name} {self.rating}% {self.year} {self.budget}'
