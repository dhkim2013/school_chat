# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-13 06:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20161113_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custumuser',
            name='profileImage',
            field=models.ImageField(default=b'/static/images/default.jpg', upload_to='profiles/'),
        ),
    ]
