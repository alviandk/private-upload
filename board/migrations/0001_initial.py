# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100, blank=True)),
                ('description', models.TextField(default=b'', blank=True)),
                ('end', models.DateField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
