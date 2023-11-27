from django import forms
from .models import Feedback


# class FeedbackForm(forms.Form):
#     name = forms.CharField(max_length=15, min_length=2, label='Имя', error_messages={
#         'required': 'ПОЛЕ ДОЛЖНО БЫТЬ ЗАПОЛНЕНО!'
#     })
#     surname = forms.CharField(required=False, label='Фамилия')
#     feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 20}), label='Текст отзыва')
#     rating = forms.IntegerField(label='Рейтинг', max_value=10, min_value=0)


class FeedbackForm(forms.ModelForm):

    class Meta:
        messages = {
            'max_length': 'ой как много символов',
            'min_length': 'ой как мало символов',
            'required': 'Не должно быть пустым'
        }
        model = Feedback
        # fields = ['name', 'surname', 'rating', 'feedback']
        fields = '__all__'
        # exclude = ['surname']
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'feedback': 'Отзыв',
            'rating': 'Рейтинг',
        }
        error_messages = {
            'name': messages,
            'surname': messages,
            'feedback': messages,
            'rating': messages,
        }

