from django.conf.urls import url
from .views import all_books, book_detail, new_book

urlpatterns = [
    url(r'^$', all_books, name='books'),
    url(r'^(?P<id>\d+)$', book_detail, name='book_detail'),
    url(r'^add$', new_book, name='new_book'),
]