# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-10 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0008_auto_20171109_0821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topiccommentmodel',
            old_name='author',
            new_name='user',
        ),
        migrations.AddField(
            model_name='topiccommentmodel',
            name='deleted_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='topicnodemodel',
            name='deleted_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='topicmodel',
            name='deleted_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]