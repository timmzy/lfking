# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-07 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='IcodropsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=20)),
                ('pricing', models.CharField(max_length=20)),
                ('tag', models.CharField(max_length=10)),
                ('expires', models.DateField()),
            ],
        ),
    ]
