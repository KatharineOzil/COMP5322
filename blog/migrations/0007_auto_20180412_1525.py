# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-12 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_category_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cover',
            field=models.ImageField(default='blog/static/category_cover/default.png', upload_to='blog/static/category_cover/'),
        ),
    ]