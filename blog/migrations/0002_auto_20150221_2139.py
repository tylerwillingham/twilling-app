# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from blog.models import Status


def create_initial_statuses(apps, schema_editor):
    """ Creates the initial statuses of: Published, Draft & Closed"""
    Status = apps.get_model('blog', 'Status')
    initial_statuses = [
        Status(
            title='Published',
            slug='published'
        ),
        Status(
            title='Draft',
            slug='draft'
        ),
        Status(
            title='Closed',
            slug='closed'
        )
    ]
    Status.objects.bulk_create(initial_statuses)


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_statuses)
    ]
