# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0002_delete_entries'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=15)),
                ('body', models.CharField(max_length=300)),
            ],
        ),
    ]
