# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from office.models import District

class Command(BaseCommand):
    help = 'Create default District'

    def handle(self, *args, **options):
        district_list = ['दार्चुला', 'कञ्चनपुर', 'डडेल्धुरा', 'कैलाली ', 'बझाङ ', 'बैतडी', 'डोटी ', 'अछाम', 'बाजुरा']
        for district in district_list:
            new_district, created = District.objects.get_or_create(district=district)
            if created:
                self.stdout.write('Successfully created district .. "%s"' % district)