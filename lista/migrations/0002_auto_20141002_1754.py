# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='describ',
            field=models.CharField(max_length=30, verbose_name=b'Categoria'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='describ',
            field=models.CharField(max_length=30, verbose_name=b'Produto'),
        ),
    ]
