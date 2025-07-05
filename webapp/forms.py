from django import forms

from webapp.models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['name', 'email', 'text']

class SearchForm(forms.Form):
    search = forms.CharField(
        label='Имя автора',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите имя автора...'
        })
    )