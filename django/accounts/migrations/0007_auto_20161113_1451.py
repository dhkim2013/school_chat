# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-13 05:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20161113_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custumuser',
            name='profileImage',
            field=models.ImageField(default='/Users/almond/Desktop/dc/static/static/default.jpg', upload_to='profiles/'),
        ),
    ]
