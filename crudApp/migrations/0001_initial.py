# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-01-06 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=20)),
                ('course', models.CharField(choices=[('python', 'Python'), ('java', 'Java'), ('django', 'Django'), ('flask', 'Flask')], max_length=10)),
                ('fee', models.FloatField()),
            ],
        ),
    ]