from django.core.validators import MinLengthValidator
from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=40, validators=[MinLengthValidator(3)])
    surname = models.CharField(max_length=40, validators=[MinLengthValidator(4)])
    feedback = models.TextField()
    rating = models.PositiveIntegerField()

