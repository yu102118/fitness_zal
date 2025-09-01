from .models import Review
from django.forms import ModelForm, TextInput, Textarea

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [ 'age', 'text']  # Только эти поля должны быть в widgets

        widgets = {
            'age': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш возраст'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш отзыв'
            }),
        }
