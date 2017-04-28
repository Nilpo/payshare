# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 20:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('purchases', '0003_add_uuid_key_to_collective'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='membership',
            unique_together=set([('member', 'collective')]),
        ),
    ]
