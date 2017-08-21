# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 06:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='karyakram',
        ),
        migrations.AddField(
            model_name='comments',
            name='comment_obj_content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notify_object', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='comments',
            name='comment_obj_object_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]