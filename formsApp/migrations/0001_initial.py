# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-01-06 11:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_num', models.IntegerField()),
                ('address', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_type', models.CharField(max_length=10)),
                ('number', models.CharField(max_length=10)),
                ('valid_until', models.DateField()),
                ('valid_from', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_type', models.CharField(max_length=10)),
                ('number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='programmer',
            name='projects',
            field=models.ManyToManyField(to='formsApp.Project'),
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='progrmmer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formsApp.Programmer'),
        ),
        migrations.AddField(
            model_name='license',
            name='programmer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='formsApp.Programmer'),
        ),
    ]
