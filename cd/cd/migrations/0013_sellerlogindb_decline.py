# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cd', '0012_sellerlogindb_imagepath'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellerlogindb',
            name='decline',
            field=models.CharField(max_length=60000, null=True),
        ),
    ]
