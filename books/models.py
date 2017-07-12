from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=254, default='')
    author = models.CharField(max_length=254, default='')
    genre = models.CharField(max_length=254, default='')
    description = models.TextField()
    ISBN = models.CharField(max_length=13, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images', default='images/default.jpg')
    
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title