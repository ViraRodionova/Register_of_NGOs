# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-05 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20160505_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='_area',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]