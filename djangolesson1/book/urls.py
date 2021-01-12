from django.urls import path
from .views import *
urlpatterns = [
    path('', books_list, name='books_list_url'),
    path('create/', book_create, name='book_create_url'),
    path('<int:id>/', book_detail, name='book_detail_url')
]
