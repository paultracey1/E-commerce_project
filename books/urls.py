from django.conf.urls import url
from .views import all_books, book_detail

urlpatterns = [
    url(r'^$', all_books, name='books'),
    url(r'^(?P<id>\d+)$', book_detail, name='book_detail'),
]