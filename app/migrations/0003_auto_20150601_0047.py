# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150601_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='sarchivo',
            name='NombreSarchivo',
            field=models.CharField(default=3, max_length=100, verbose_name=b'Nombre contenido'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contenido',
            name='Mangas',
            field=models.ManyToManyField(to='app.Manga', blank=True),
        ),
        migrations.AlterField(
            model_name='contenido',
            name='Videos',
            field=models.ManyToManyField(to='app.Video', blank=True),
        ),
        migrations.AlterField(
            model_name='sarchivo',
            name='PaginasDuracion',
            field=models.IntegerField(verbose_name=b'Paginas o Duracion'),
        ),
    ]
