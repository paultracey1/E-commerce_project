# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 09:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20170712_1025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Category',
            new_name='genre',
        ),
    ]
