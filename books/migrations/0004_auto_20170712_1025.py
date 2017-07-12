# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_genre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='genre',
            new_name='Category',
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images'),
        ),
    ]