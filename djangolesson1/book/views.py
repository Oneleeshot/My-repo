from django.shortcuts import render, redirect
from .models import Book
from django.views.generic import DetailView, CreateView, ListView


# def books_list(request):
#     books = Book.objects.all()
#     return render(request, 'book/index.html', context={'books': books})

class BookListView(ListView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BookCreate(CreateView):
    model = Book
    fields = ['title', 'author_name', 'description']
    template_name_suffix = '_create_form'


class BookDetailView(DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# def book_create(request):
#     error = ''
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('books_list_url')
#         else:
#             error = '123'
#     form = BookForm()
#     return render(request, 'book/book_create_form.html',
#                   context={'form': form, 'error': error})

# def book_detail(request, id):
#     book = Book.objects.get(id=id)
#     return render(request, 'book/book_detail.html', context={'book': book})
