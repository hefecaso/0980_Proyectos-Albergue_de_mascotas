from django.shortcuts import render, HttpResponse

from .forms import CustomUserCreationForm, ContactoForm

from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings
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

#formulario registro
def formulario_registro_mascota(request):
    return render(request, "pagina1app/formulario_registro_mascota.html")

#opción general: este no es un formulario solo reedirecciona al TEMPLATE
def registro_y_adopcion(request):
    return render(request, "pagina1app/registro_y_adopcion.html")

#formulario adopta
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

    #    subject=request.POST["tipo_consulta"]
    #    message=request.POST["Mensaje"] + " " + request.POST["Correo"]
    #    email_from=settings.EMAIL_HOST_USER
    #    recipient_list=["alberguemascotas93@gmail.com"]
    #    send_mail(subject, message, email_from, recipient_list)
    data = {'form': ContactoForm()}
    if request.method == 'POST':
        subject=request.POST["nombre"]
        message=request.POST["mensaje"] + " " + request.POST["correo"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["alberguemascotas93@gmail.com"]
        send_mail(subject, message, email_from, recipient_list)
        #Si me enviaron datos, crear nuevo formulario con los datos enviados
        formulario = ContactoForm(data=request.POST) #POST es un diccionario con todos los datos

        if formulario.is_valid(): #Validando
            formulario.save()
            data["mensaje"] = "Mensaje enviado, pronto alguno de nuestros operadores se comunicará contigo"

        else: #Si no valida
            data["form"] = formulario


    return render(request, "pagina1app/contacto.html", data)
