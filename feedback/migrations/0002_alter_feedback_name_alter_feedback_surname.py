# Generated by Django 4.2.7 on 2023-11-27 13:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='surname',
            field=models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
    ]
