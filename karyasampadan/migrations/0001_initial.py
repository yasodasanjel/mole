# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 07:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('office', '0004_auto_20170719_0702'),
        ('reports', '0015_auto_20170727_0618'),
    ]

    operations = [
        migrations.CreateModel(
            name='SampadanKaryakram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u0938\u0942\u091a\u0915')),
                ('fiscal_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.FiscalYear', verbose_name='\u0935\u093f\u0924\u094d\u0924\u0940\u092f \u0935\u0930\u094d\u0937')),
                ('main_suchak', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='karyasampadan_parent', to='karyasampadan.SampadanKaryakram', verbose_name='\u092e\u0941\u0916\u094d\u092f \u0938\u0942\u091a\u0915')),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office.Office', verbose_name='\u0928\u093f\u0915\u093e\u092f')),
            ],
        ),
        migrations.CreateModel(
            name='SampadanMonthlyProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pragati', models.TextField(verbose_name='\u092e\u0939\u093f\u0928\u093e\u0915\u094b \u092a\u094d\u0930\u0917\u0924\u0940')),
                ('pragati_till_date', models.TextField(verbose_name='\u0939\u093e\u0932 \u0938\u092e\u094d\u092e\u0915\u094b \u092a\u094d\u0930\u0917\u0924\u0940')),
                ('comments', models.TextField(verbose_name='\u0915\u0948\u092b\u093f\u092f\u0924')),
                ('datesubmited', models.CharField(blank=True, max_length=10, null=True)),
                ('dateupdated', models.CharField(blank=True, max_length=10, null=True)),
                ('fiscal_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.FiscalYear', verbose_name='\u0935\u093f\u0924\u094d\u0924\u0940\u092f \u0935\u0930\u094d\u0937')),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.Months')),
                ('sampadan_karyakram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sampadan_monthlyprogress', to='karyasampadan.SampadanKaryakram', verbose_name=' \u0915\u093e\u0930\u094d\u092f\u0915\u094d\u0930\u092e')),
            ],
        ),
    ]