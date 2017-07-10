from __future__ import unicode_literals

from django.db import models
from products.models import Product
from books.models import Book
from django.contrib.auth.models import User

# Create your models here.
class CartItem(models.Model):
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)
    quantity = models.IntegerField()

    def __str__(self):
        return "{0} ({1})".format(self.book.name, self.quantity)