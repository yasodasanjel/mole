# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 06:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supa', '0002_auto_20170531_0630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='office',
            name='category',
        ),
    ]
