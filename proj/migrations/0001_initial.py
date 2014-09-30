# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=60, verbose_name=b'Nome')),
                ('email', models.EmailField(max_length=75, verbose_name=b'E-mail')),
                ('endereco', models.CharField(max_length=60, verbose_name=b'Endere\xc3\xa7o')),
                ('senha', models.CharField(max_length=60, verbose_name=b'Senha')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codBarra', models.CharField(max_length=20, verbose_name=b'Cod. Barra')),
                ('descricao', models.CharField(max_length=60, verbose_name=b'Descri\xc3\xa7\xc3\xa3o')),
                ('fabricante', models.CharField(max_length=60, verbose_name=b'Fabricante')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='lista',
            name='produto',
            field=models.ManyToManyField(related_name=b'Cotacao', to='proj.Produto'),
            preserve_default=True,
        ),
    ]
