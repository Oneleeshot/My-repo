from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def books_list(request):
    books = Book.objects.all()
    return render(request, 'book/index.html', context={'books': books})


def book_create(request):
    error = ''
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books_list_url')
        else:
            error = '123'
    form = BookForm()
    return render(request, 'book/book_create_form.html',
                  context={'form': form, 'error': error})


def book_detail(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'book/book_detail.html', context={'book': book})
