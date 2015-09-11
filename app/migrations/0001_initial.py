# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contenido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NombreContenido', models.CharField(max_length=100)),
                ('AutorContenido', models.CharField(max_length=100)),
                ('DescripcionContenido', models.CharField(max_length=100)),
                ('EstiloContenido', models.CharField(max_length=100)),
                ('ImagenContenido', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FechaPublicacionVideos', models.DateField()),
                ('FechaSubidaVideos', models.DateField()),
                ('PaginasManga', models.IntegerField()),
                ('ImagenManga', models.ImageField(upload_to=b'')),
                ('LinkDescargaManga', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(max_length=100)),
                ('Rut', models.IntegerField()),
                ('NombreUsuario', models.CharField(max_length=100)),
                ('Contrasena', models.CharField(max_length=100)),
                ('FechaNacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254, verbose_name=b'e-mail', blank=True)),
                ('Telefono', models.IntegerField()),
                ('Direccion', models.CharField(max_length=100)),
                ('Moderador', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Sarchivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FechaPublicacion', models.DateField()),
                ('FechaSubida', models.DateField()),
                ('PaginasDuracion', models.IntegerField()),
                ('Imagen', models.ImageField(upload_to=b'')),
                ('LinkDescarga', models.URLField()),
                ('contenido', models.ForeignKey(to='app.Contenido')),
            ],
        ),
        migrations.CreateModel(
            name='Scontenido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NombreContenidoS', models.CharField(max_length=100)),
                ('AutorContenidoS', models.CharField(max_length=100)),
                ('DescripcionContenidoS', models.CharField(max_length=100)),
                ('EstiloContenidoS', models.CharField(max_length=100)),
                ('ImagenContenidoS', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FechaPublicacionVideo', models.DateField()),
                ('FechaSubidaVideo', models.DateField()),
                ('DuracionVideo', models.IntegerField()),
                ('ImagenVideo', models.ImageField(upload_to=b'')),
                ('LinkDescargaVideo', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='contenido',
            name='Mangas',
            field=models.ManyToManyField(to='app.Manga'),
        ),
        migrations.AddField(
            model_name='contenido',
            name='Videos',
            field=models.ManyToManyField(to='app.Video'),
        ),
    ]
