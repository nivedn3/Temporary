# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-10 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cd', '0007_auto_20160310_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerlogindb',
            name='category',
            field=models.BigIntegerField(default=1),
        ),
    ]
