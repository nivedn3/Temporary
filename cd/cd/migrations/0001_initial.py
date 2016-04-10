# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-06 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sellerlogin',
            fields=[
                ('user', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('mobile', models.IntegerField()),
                ('shopname', models.CharField(max_length=80)),
                ('shopid', models.CharField(max_length=80)),
                ('office_no', models.IntegerField()),
                ('city', models.CharField(max_length=200)),
                ('Address1', models.CharField(max_length=200)),
                ('Address2', models.CharField(max_length=200)),
                ('category', models.BigIntegerField()),
                ('gcmid', models.CharField(max_length=1000)),
                ('token', models.CharField(max_length=100)),
                ('gps', models.CharField(max_length=100)),
            ],
        ),
    ]