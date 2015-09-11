
var direccionesRoc=new Array();
var direccionesAca=new Array();
direccionesRoc[0]="rock1.htm";
direccionesRoc[1]="rock2.htm";
direccionesAca[0]="barroco.htm";
direccionesAca[1]="sigloxx.htm";
direccionesAca[2]="romantico.htm";

function direccion(form){
var selec = form.tipos.options;
var combo = form.estilo.options;
    if (selec[1].selected == true){
	     document.form.action=direccionesRoc[combo.selectedIndex];
	}
    if (selec[2].selected == true){
	     form.action=direccionesAca[combo.selectedIndex];
	}

        /*Se puede quitar una vez vemos que funciona*/
	alert(form.action);

}



function agregarOpciones(form)
{
var selec = form.tipos.options;
var combo = form.estilo.options;
combo.length = null;

    if (selec[0].selected == true)
    {
    var seleccionar = new Option("Esperando selección");
    combo[0] = seleccionar;
    }

    if (selec[1].selected == true)
    {
    var popular1 = new Option("Rock de los 90");
    var popular2 = new Option("Rock de los 80");
    combo[0] = popular1;
    combo[1] = popular2;
    }

    if (selec[2].selected == true)
    {
    var academica1 = new Option("Musica del Barroco");
    var academica2 = new Option("Musica del Siglo XX");
    var academica3 = new Option("Música del Romantisismo");
    combo[0] = academica1;
    combo[1] = academica2;
    combo[2] = academica3;
    }
}

function muestra_oculta(id){
if (document.getElementById){ //se obtiene el id
var el = document.getElementById(id); //se define la variable "el" igual a nuestro div
if(el == usado)
{
	el.style.display = (el.style.display == 'none') ? 'block' : 'none'; //damos un atributo display:none que oculta el div
	if(nuevo.style.display == 'none')
	{

	}else{
		nuevo.style.display ='none';
	}
}
else if(el == nuevo)
{
	el.style.display = (el.style.display == 'none') ? 'block' : 'none'; //damos un atributo display:none que oculta el div
	if(usado.style.display == 'none')
	{
	
	}else{
		usado.style.display ='none';
	}

}
else if(el == credito)
{
	el.style.display = (el.style.display == 'none') ? 'block' : 'none'; //damos un atributo display:none que oculta el div
	if(contado.style.display == 'none')
	{
	
	}else{
		contado.style.display ='none';
	}

}
else if(el == contado)
{
	el.style.display = (el.style.display == 'none') ? 'block' : 'none'; //damos un atributo display:none que oculta el div
	if(credito.style.display == 'none')
	{
	
	}else{
		credito.style.display ='none';
	}

}

}
}

window.onload = function(){/*hace que se cargue la función lo que predetermina que div estará oculto hasta llamar a la función nuevamente*/
muestra_oculta('contenido_a_mostrar');/* "contenido_a_mostrar" es el nombre que le dimos al DIV */
}
