# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 10:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('office', '0001_initial'),
        ('reports', '0010_auto_20170715_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='SachibBaithak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datesubmited', models.CharField(blank=True, max_length=10, null=True)),
                ('dateupdated', models.CharField(blank=True, max_length=10, null=True)),
                ('nirnayaharu', models.TextField(verbose_name='\u0928\u093f\u0930\u094d\u0923\u092f\u0939\u0930\u0941')),
                ('jimmewar_nikaya', models.CharField(max_length=100, verbose_name='\u091c\u093f\u092e\u094d\u092e\u0947\u0935\u093e\u0930 \u0928\u093f\u0915\u093e\u092f')),
                ('karyanayan_awastha', models.TextField(verbose_name='\u0915\u093e\u0930\u094d\u092f\u093e\u0928\u094d\u0935\u092f\u0928 \u0905\u0935\u0938\u094d\u0925\u093e')),
                ('samaya_sima', models.CharField(max_length=100, verbose_name='\u0938\u092e\u092f \u0938\u093f\u092e\u093e ')),
                ('fiscal_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.FiscalYear', verbose_name='\u0935\u093f\u0924\u094d\u0924\u0940\u092f \u0935\u0930\u094d\u0937')),
            ],
        ),
    ]
