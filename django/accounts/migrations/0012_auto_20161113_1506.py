# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-13 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20161113_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custumuser',
            name='profileImage',
            field=models.ImageField(default=b'/static/profiles/default.jpg', upload_to=b'/static/profiles/'),
        ),
    ]
