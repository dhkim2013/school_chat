# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20161101_1939'),
        ('class_room', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student',
        ),
        migrations.RemoveField(
            model_name='class',
            name='students',
        ),
        migrations.AddField(
            model_name='class',
            name='students',
            field=models.ManyToManyField(null=True, to='accounts.CustumUser'),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
