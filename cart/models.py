from __future__ import unicode_literals

from django.db import models
from books.models import Book
from django.contrib.auth.models import User

# Create your models here.
class CartItem(models.Model):
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)

    def __str__(self):
        return "{0}".format(self.book.title)