# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-02 06:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinkslips', '0003_auto_20180302_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='/media'),
        ),
    ]
