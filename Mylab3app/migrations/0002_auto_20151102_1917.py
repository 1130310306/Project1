# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mylab3app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='PublishDate',
            field=models.CharField(max_length=40),
        ),
    ]
