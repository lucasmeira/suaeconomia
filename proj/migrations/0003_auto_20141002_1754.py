# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0002_auto_20141001_2041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lista',
            old_name='produto',
            new_name='produtos',
        ),
        migrations.AddField(
            model_name='lista',
            name='cliente',
            field=models.OneToOneField(related_name=b'lCliente', default=b'1', to='proj.Cliente'),
            preserve_default=True,
        ),
    ]
