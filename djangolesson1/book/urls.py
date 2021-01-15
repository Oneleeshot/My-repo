from django.urls import path
from .views import *
urlpatterns = [
    path('', BookListView.as_view(), name='books_list_url'),
    path('create/', BookCreate.as_view(), name='book_create_url'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail_url')
]
