# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-11 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='num_vote_down',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='image',
            name='num_vote_up',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='image',
            name='vote_score',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]