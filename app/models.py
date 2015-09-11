from django.db import models

class Video(models.Model):
    NombreVideo = models.CharField('Nombre video',max_length=100)
    FechaPublicacionVideo = models.DateField('Fecha publicacion video')
    FechaSubidaVideo = models.DateField('Fecha subida video')
    DuracionVideo = models.IntegerField('Duracion video')
    ImagenVideo = models.ImageField('Imagen video')
    LinkDescargaVideo = models.URLField('Link descarga video')
    def __unicode__(self):
        return (self.NombreVideo)
    
    
    
class Manga(models.Model):
    NombreManga = models.CharField('Nombre manga',max_length=100)
    FechaPublicacionVideos = models.DateField('Fecha publicacion video')
    FechaSubidaVideos = models.DateField('Fecha subida video')
    PaginasManga = models.IntegerField('Paginas manga')
    ImagenManga = models.ImageField('Imagen manga')
    LinkDescargaManga = models.URLField('Link descarga manga')
    def __unicode__(self):
        return (self.NombreManga)
    
        
class Persona(models.Model):
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Rut = models.IntegerField()
    NombreUsuario = models.CharField('Nombre usaurio',max_length=100)
    Contrasena = models.CharField(max_length=100)
    FechaNacimiento = models.DateField('Fecha nacimiento')
    email = models.EmailField('e-mail', blank=True)
    Telefono = models.IntegerField()
    Direccion = models.CharField(max_length=100)
    Moderador = models.BooleanField()
    def __unicode__(self):
        return '%s'%(self.NombreUsuario)

class Scontenido(models.Model):
    NombreContenidoS = models.CharField('Nombre contenido',max_length=100)
    AutorContenidoS = models.CharField('Autor contenido',max_length=100)
    DescripcionContenidoS = models.CharField('Descripcion contenido',max_length=100)
    EstiloContenidoS = models.CharField('Estilo contenido',max_length=100)
    ImagenContenidoS = models.URLField('Link descarga')
    def __unicode__(self):
        return (self.NombreContenidoS)

class Contenido(models.Model):
    NombreContenido = models.CharField('Nombre contenido',max_length=100)
    AutorContenido = models.CharField('Autor contenido',max_length=100)
    DescripcionContenido = models.CharField('Descripcion contenido',max_length=100)
    EstiloContenido = models.CharField('Estilo contenido',max_length=100)
    ImagenContenido = models.URLField('Link descarga')
    Videos = models.ManyToManyField(Video,blank=True)
    Mangas = models.ManyToManyField(Manga,blank=True)
    def __unicode__(self):
        return (self.NombreContenido)
    

class Sarchivo(models.Model):
    NombreSarchivo = models.CharField('Nombre contenido',max_length=100)
    FechaPublicacion = models.DateField('Fecha publicacion')
    FechaSubida = models.DateField('Fecha subida')
    PaginasDuracion = models.IntegerField('Paginas o Duracion')
    Imagen = models.ImageField()
    LinkDescarga = models.URLField('Link descarga')
    contenido = models.ForeignKey(Contenido)
    def __unicode__(self):
        return (self.NombreSarchivo)
    
    
