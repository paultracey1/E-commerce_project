from django.conf.urls import url
from .views import root_categories, get_category
from books.views import *
from . import views

urlpatterns = [
    url(r'^$', root_categories, name='categories'),
    url(r'^(?P<id>\d+)$', book_detail),
]