# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 12:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cd', '0020_auto_20160402_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selldb',
            name='bprice',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AlterField(
            model_name='selldb',
            name='btime',
            field=models.BigIntegerField(default=0),
        ),
    ]
