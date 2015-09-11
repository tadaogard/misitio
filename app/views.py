from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render, render_to_response
from app.models import Manga,Persona,Video,Contenido,Scontenido,Sarchivo
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime
from django.template.context import RequestContext
from forms import PersonaForm
from django.core.context_processors import csrf
from email import email


def Base(request):
    
    mangas = Manga.objects.filter()
    series = Video.objects.filter()
    return render(request, 'base.html',
            {'mangas': mangas,'series':series})
 
 
 
    
def buscar(request):
    return render(request, 'busqueda.html')
      


def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

# GOOD (VERSION 2)
def ua_display_good2(request):
    ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    return HttpResponse("Your browser is %s" % ua)

def search_form(request):
    return render(request, 'search_form.html')

def contacto(request):
    return render(request, 'contactanos.html')


@login_required(redirect_field_name='/')
def contenido(request):
    errors = []
    if 'cont' in request.GET:
        c = request.GET['cont']
        if not c:
            errors.append('No contenido')
        else:
            contenido = Contenido.objects.get(NombreContenido=c)
            return render(request, 'contenido.html',
                          {'Contenido': contenido, 'Mangas': "b", 'Series': "c"})
    return render(request, 'contenido.html',
                  {'errors': errors})

@login_required(redirect_field_name='/')
def search(request):
    errors = []
    if 'busq' in request.GET:
        q = request.GET['busq']
        if not q:
            errors.append('Ingrese algun termino a buscar')
        elif len(q) > 20:
            errors.append('Por favor ingrese hasta 20 caracteres')
        else:
            books = Contenido.objects.filter(NombreContenido__icontains=q)
            return render(request, 'busqueda.html',
                {'series': books, 'query': q})
    return render(request, 'busqueda.html',
        {'errors': errors})

def login(request):
    username = request.GET['nombre']
    password = request.GET['pass']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            usuario =  Persona.objects.get(NombreUsuario=username)
            return render(request, 'cuenta.html',
                                {'book': usuario})
        else:
            #return disable acount#
            return render(request, 'base.html',
                      {'errors': "Cuenta Deshabilitada"})
            
    else:
        #return invalid login
        return render(request, 'base.html',
                      {'errors': "Error en el usuario o contrasena"})

def registrar(request):
    if request.method=='POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/base/')
    else:
        form = PersonaForm()
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = form

    return render_to_response('crearCuenta.html', args)


def registrando(request):
    if request.method=='POST':
            nombre = request.POST['Nombre']
            apellido = request.POST['Apellido']
            rut = request.POST['Rut']
            usuario = request.POST['NombreUsuario']
            contrasena = request.POST['Contrasena']
            email = request.POST['email']
            telefono = request.POST['Telefono']
            direccion = request.POST['Direccion']
            fechanacimiento = request.POST['FechaNacimiento']
            
            # registro en la bdd
            a = Persona(Nombre=nombre, Apellido=apellido, Rut=rut,
                        NombreUsuario=usuario, Contrasena=contrasena,
                         email=email, Moderador= 0,
                        Telefono=telefono, Direccion=direccion, FechaNacimiento= fechanacimiento)
            a.save()
            
            # registro en el autentificador para encriptar la pass 
            usera = User.objects.create_user(usuario, email, contrasena)
            user = authenticate(username=usuario, password=contrasena)
            
            auth.login(request, user)
            resultado=  Persona.objects.get(NombreUsuario=usuario)
            
            
            return render(request, 'cuenta.html',
                                {'book': resultado})

    
