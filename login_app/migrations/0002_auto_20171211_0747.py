# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-11 07:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userregisterdetails',
            old_name='age',
            new_name='password',
        ),
    ]
