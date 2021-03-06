# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-12 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cd', '0010_auto_20160312_0906'),
    ]

    operations = [
        migrations.CreateModel(
            name='selldb',
            fields=[
                ('Cus_id', models.CharField(max_length=30)),
                ('Q_price', models.CharField(max_length=50)),
                ('Sel_type', models.IntegerField(default=False)),
                ('Sel_comments', models.CharField(max_length=500)),
                ('Sel_deltype', models.IntegerField(default=False)),
                ('Cus2_conf', models.IntegerField(default=False)),
                ('Sel2_conf', models.IntegerField(default=False)),
                ('img_path', models.CharField(max_length=100, null=True)),
                ('Sel_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='request_conf',
            name='Cus2_conf',
        ),
        migrations.RemoveField(
            model_name='request_conf',
            name='Sel2_conf',
        ),
        migrations.RemoveField(
            model_name='request_conf',
            name='Sel_comments',
        ),
        migrations.RemoveField(
            model_name='request_conf',
            name='Sel_deltype',
        ),
        migrations.RemoveField(
            model_name='request_conf',
            name='Sel_type',
        ),
        migrations.RemoveField(
            model_name='request_conf',
            name='img_path',
        ),
        migrations.AddField(
            model_name='request_conf',
            name='Cus_email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='request_conf',
            name='Cus_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
