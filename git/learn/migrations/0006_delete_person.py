# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-20 07:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0005_user_enabled'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]
