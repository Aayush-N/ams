# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-30 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_merge_20180730_0728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='absentees',
            old_name='name',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
