# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wbs_user', '0003_bookingsession_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingsession',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]