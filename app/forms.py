from django import forms
from models import Persona

class PersonaForm(forms.ModelForm):
    
    class Meta:
        model = Persona
        fields = ('Nombre', 'Apellido', 'Rut', 'NombreUsuario', 'Contrasena', 'FechaNacimiento', 'email', 'Telefono', 'Direccion')