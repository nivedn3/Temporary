# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-06 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerlogin',
            name='category',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sellerlogin',
            name='office_no',
            field=models.IntegerField(null=True),
        ),
    ]
