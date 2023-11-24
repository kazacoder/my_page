from django.db import models
from django.urls import reverse
from pytils.translit import slugify
# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True)
    budget = models.IntegerField(default=1_000_000)
    slug = models.SlugField(default='', null=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('movie', args=(self.slug, ))

    def __str__(self):
        return f'{self.name} {self.rating}% {self.year} {self.budget}'
