# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='NombreManga',
            field=models.CharField(default=3, max_length=100, verbose_name=b'Nombre manga'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='NombreVideo',
            field=models.CharField(default=4, max_length=100, verbose_name=b'Nombre video'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contenido',
            name='AutorContenido',
            field=models.CharField(max_length=100, verbose_name=b'Autor contenido'),
        ),
        migrations.AlterField(
            model_name='contenido',
            name='DescripcionContenido',
            field=models.CharField(max_length=100, verbose_name=b'Descripcion contenido'),
        ),
        migrations.AlterField(
            model_name='contenido',
            name='EstiloContenido',
            field=models.CharField(max_length=100, verbose_name=b'Estilo contenido'),
        ),
        migrations.AlterField(
            model_name='contenido',
            name='ImagenContenido',
            field=models.ImageField(upload_to=b'', verbose_name=b'Imagen contenido'),
        ),
        migrations.AlterField(
            model_name='contenido',
            name='NombreContenido',
            field=models.CharField(max_length=100, verbose_name=b'Nombre contenido'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='FechaPublicacionVideos',
            field=models.DateField(verbose_name=b'Fecha publicacion video'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='FechaSubidaVideos',
            field=models.DateField(verbose_name=b'Fecha subida video'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='ImagenManga',
            field=models.ImageField(upload_to=b'', verbose_name=b'Imagen manga'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='LinkDescargaManga',
            field=models.URLField(verbose_name=b'Link descarga manga'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='PaginasManga',
            field=models.IntegerField(verbose_name=b'Paginas manga'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='FechaNacimiento',
            field=models.DateField(verbose_name=b'Fecha nacimiento'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='NombreUsuario',
            field=models.CharField(max_length=100, verbose_name=b'Nombre usaurio'),
        ),
        migrations.AlterField(
            model_name='sarchivo',
            name='FechaPublicacion',
            field=models.DateField(verbose_name=b'Fecha publicacion'),
        ),
        migrations.AlterField(
            model_name='sarchivo',
            name='FechaSubida',
            field=models.DateField(verbose_name=b'Fecha subida'),
        ),
        migrations.AlterField(
            model_name='sarchivo',
            name='LinkDescarga',
            field=models.URLField(verbose_name=b'Link descarga'),
        ),
        migrations.AlterField(
            model_name='sarchivo',
            name='PaginasDuracion',
            field=models.IntegerField(verbose_name=b'Duracion'),
        ),
        migrations.AlterField(
            model_name='scontenido',
            name='AutorContenidoS',
            field=models.CharField(max_length=100, verbose_name=b'Autor contenido'),
        ),
        migrations.AlterField(
            model_name='scontenido',
            name='DescripcionContenidoS',
            field=models.CharField(max_length=100, verbose_name=b'Descripcion contenido'),
        ),
        migrations.AlterField(
            model_name='scontenido',
            name='EstiloContenidoS',
            field=models.CharField(max_length=100, verbose_name=b'Estilo contenido'),
        ),
        migrations.AlterField(
            model_name='scontenido',
            name='ImagenContenidoS',
            field=models.ImageField(upload_to=b'', verbose_name=b'Imagen contenido'),
        ),
        migrations.AlterField(
            model_name='scontenido',
            name='NombreContenidoS',
            field=models.CharField(max_length=100, verbose_name=b'Nombre contenido'),
        ),
        migrations.AlterField(
            model_name='video',
            name='DuracionVideo',
            field=models.IntegerField(verbose_name=b'Duracion video'),
        ),
        migrations.AlterField(
            model_name='video',
            name='FechaPublicacionVideo',
            field=models.DateField(verbose_name=b'Fecha publicacion video'),
        ),
        migrations.AlterField(
            model_name='video',
            name='FechaSubidaVideo',
            field=models.DateField(verbose_name=b'Fecha subida video'),
        ),
        migrations.AlterField(
            model_name='video',
            name='ImagenVideo',
            field=models.ImageField(upload_to=b'', verbose_name=b'Imagen video'),
        ),
        migrations.AlterField(
            model_name='video',
            name='LinkDescargaVideo',
            field=models.URLField(verbose_name=b'Link descarga video'),
        ),
    ]
