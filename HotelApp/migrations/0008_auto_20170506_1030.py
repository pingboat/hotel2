# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApp', '0007_hotels_partner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='TelephoneNumber',
            field=models.CharField(max_length=12),
        ),
    ]
