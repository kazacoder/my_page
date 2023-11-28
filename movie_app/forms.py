from django import forms
from .models import Director, Movie

choice = tuple((ds.id, f'{ds.first_name} {ds.last_name}') for ds in list(Director.objects.all()))


# class AddMovieForm(forms.Form):
#     name = forms.CharField(max_length=40, label='Название', error_messages={
#         'required': 'ПОЛЕ ДОЛЖНО БЫТЬ ЗАПОЛНЕНО!'
#     })
#     rating = forms.IntegerField(label='Рейтинг', max_value=100, min_value=0)
#     year = forms.IntegerField(label='Год', max_value=2500, min_value=1900)
#     budget = forms.IntegerField(label='Бюджет', max_value=100_000_000_000)
#     director = forms.ChoiceField(label='Режиссер', required=False, choices=choice)


class AddMovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        exclude = ['slug', 'currency']
        labels = {
            'name': 'Название',
            'rating': 'Рейтинг',
            'year': 'Год',
            'budget': 'Бюджет',
            'slug': 'Слаг',
            'currency': 'Валюта',
            'director': 'Режиссер',
            'actors': 'Актеры',
        }
