# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lista',
            name='nome',
            field=models.CharField(default=b'Nome da Lista', max_length=40, verbose_name=b'Nome'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lista',
            name='produto',
            field=models.ManyToManyField(related_name=b'lista+', to=b'proj.Produto'),
        ),
    ]
