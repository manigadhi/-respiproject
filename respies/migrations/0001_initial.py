# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recipie_name', models.CharField(max_length=200)),
                ('ingrediants', models.CharField(max_length=500)),
                ('process', models.TextField(max_length=1000)),
            ],
        ),
    ]
