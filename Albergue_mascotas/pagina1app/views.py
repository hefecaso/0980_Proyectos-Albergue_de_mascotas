from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from .forms import CustomUserCreationForm, ContactoForm, Registro_mascota_Form

from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

# Create your views here.


def home(request):
    return render(request, "pagina1app/home.html")


def servicios(request):
    return render(request, "pagina1app/servicios.html")


def albergue(request):
    return render(request, "pagina1app/albergue.html")


'''
def iniciosesion(request):
    return render(request, "pagina1app/iniciosesion.html")
'''

'''
def contacto(request):
    return render(request, "pagina1app/contacto.html")
'''


def formulario_registro_mascota(request):
    return render(request, "pagina1app/formulario_registro_mascota.html")


def registro_y_adopcion(request):
    return render(request, "pagina1app/registro_y_adopcion.html")


def formulario_adopcion(request):
    return render(request, "pagina1app/formulario_adopcion.html")


#############################################
#   Configurando el registro de usuario     #
#############################################
id


def registro(request):
    data = {'form': CustomUserCreationForm()}

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            # Autenticando al usuario
            user = authenticate(
                username=formulario.cleaned_data['username'], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            # Redirigiendo a Home
            return redirect(to="Home")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)


#############################################
#   Configurando el registro para Contacto  #
#############################################

def contacto(request):
    data = {'form': ContactoForm()}

    if request.method == 'POST':
        #Si me enviaron datos, crear nuevo formulario con los datos enviados
        formulario = ContactoForm(data=request.POST) #POST es un diccionario con todos los datos

        if formulario.is_valid(): #Validando
            formulario.save()
            data["mensaje"] = "Mensaje enviado, pronto alguno de nuestros operadores se comunicará contigo"
        else: #Si no valida
            data["form"] = formulario

    return render(request, "pagina1app/contacto.html", data)

#####################################################
#   Configurando el registro para registro mascota  #
#####################################################

def formulario_registro_mascota(request):

    if request.method == 'POST':
        #Si me enviaron datos, crear nuevo formulario con los datos enviados
        form = Registro_mascota_Form(request.POST) #POST es un diccionario con todos los datos

        if form.is_valid(): #Validando
            form.save()
            mensaje = "Registro completado"
            print("Registro correcto")

        return redirect('Formulario registro')

    else: #Si no valida
        form = Registro_mascota_Form()
        print("Error")

    return render(request, "pagina1app/formulario_registro_mascota.html", {'form':form})
