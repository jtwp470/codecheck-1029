# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-13 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=255, null=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateField()),
            ],
        ),
    ]
