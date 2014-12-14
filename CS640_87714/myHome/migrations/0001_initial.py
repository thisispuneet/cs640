# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DEVELOPMENT',
            fields=[
                ('name', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('content', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PRODUCTION',
            fields=[
                ('name', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('content', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
