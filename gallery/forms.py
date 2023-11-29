from django import forms
from .models import Gallery


class GalleryUploadForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'
        labels = {'file': 'Файл'}
        error_messages = {'file': {'required': 'ПОЛЕ ДОЛЖНО БЫТЬ ЗАПОЛНЕНО!'}}
