# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-10 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cd', '0008_auto_20160310_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='request_conf',
            name='img_path',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
