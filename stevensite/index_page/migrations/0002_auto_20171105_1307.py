# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linktopoststatic',
            name='name_text',
            field=models.CharField(default='name', max_length=50, primary_key=True, serialize=False),
        ),
    ]