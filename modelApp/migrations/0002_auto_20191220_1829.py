# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-20 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone_num',
            field=models.IntegerField(),
        ),
    ]
