from __future__ import unicode_literals

from django.db import models
from books.models import Book

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True)
    books = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return self.name