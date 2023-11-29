from django.db import models

# Create your models here.


class Gallery(models.Model):
    file = models.FileField(upload_to='gallery')
