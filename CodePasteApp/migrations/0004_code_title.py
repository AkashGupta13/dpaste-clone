# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CodePasteApp', '0003_auto_20170626_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='title',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
