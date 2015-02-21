# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150221_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, max_length=70),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(unique=True, max_length=70),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True, max_length=125),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(unique=True, max_length=125),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='status',
            name='slug',
            field=models.SlugField(unique=True, max_length=70),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='status',
            name='title',
            field=models.CharField(unique=True, max_length=70),
            preserve_default=True,
        ),
    ]
