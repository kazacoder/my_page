from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=15, min_length=2, label='Имя', error_messages={
        'required': 'ПОЛЕ ДОЛЖНО БЫТЬ ЗАПОЛНЕНО!'
    })
    surname = forms.CharField(required=False, label='Фамилия')
    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 20}), label='Текст отзыва')
    rating = forms.IntegerField(label='Рейтинг', max_value=10, min_value=0)




