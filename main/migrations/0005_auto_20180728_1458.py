# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-28 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_changestatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absentees',
            name='attendance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='absentee', to='main.Attendance'),
        ),
    ]