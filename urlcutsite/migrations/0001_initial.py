# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 22:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('short_id', models.SlugField(primary_key=True, serialize=False)),
                ('url', models.URLField(max_length=2000)),
                ('counter', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('submitter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
