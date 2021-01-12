from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author_name', 'description']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }
