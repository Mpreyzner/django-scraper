# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-11 21:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authorstats',
            name='top_10_words',
        ),
        migrations.RemoveField(
            model_name='totalstats',
            name='top_10_words',
        ),
    ]
