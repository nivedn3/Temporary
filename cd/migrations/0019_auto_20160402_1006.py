# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 10:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cd', '0018_auto_20160331_1324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adv',
            old_name='adv',
            new_name='advt',
        ),
    ]