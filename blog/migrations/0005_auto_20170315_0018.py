# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-14 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170315_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pic',
            field=models.ImageField(upload_to='C:\\djangogirls\x08log\templates\x08log'),
        ),
    ]
