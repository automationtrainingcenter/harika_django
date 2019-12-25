# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-25 05:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelApp', '0005_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_type', models.CharField(max_length=10)),
                ('number', models.CharField(max_length=10)),
                ('valid_until', models.DateField()),
                ('valid_from', models.DateField(auto_now_add=True)),
                ('programmer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='modelApp.Programmer')),
            ],
        ),
    ]