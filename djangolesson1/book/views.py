from django.shortcuts import render, redirect
from .models import Book
from django.views.generic import DetailView, CreateView, ListView


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

