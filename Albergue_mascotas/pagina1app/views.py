from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):

    return HttpResponse("home")

def servicios(request):

    return HttpResponse("servicios")

def albergue(request):

    return HttpResponse("albergue")

def iniciosesion(request):

    return HttpResponse("iniciosesion")

def contacto(request):

    return HttpResponse("contacto")
