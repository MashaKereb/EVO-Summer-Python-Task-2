# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 10:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='desc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Description'),
        ),
    ]