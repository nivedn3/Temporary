# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cd', '0013_sellerlogindb_decline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerlogindb',
            name='decline',
            field=models.CharField(default='123', max_length=60000),
        ),
    ]
