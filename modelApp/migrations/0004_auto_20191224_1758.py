# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-24 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelApp', '0003_programmer_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='programmers',
        ),
        migrations.AddField(
            model_name='programmer',
            name='projects',
            field=models.ManyToManyField(to='modelApp.Project'),
        ),
    ]
