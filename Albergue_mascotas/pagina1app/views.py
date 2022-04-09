from django.shortcuts import render, HttpResponse

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

def contacto(request):
    return render(request, "pagina1app/contacto.html")

def formulario_registro_mascota(request):
    return render(request, "pagina1app/formulario_registro_mascota.html")

def registro_y_adopcion(request):
    return render(request, "pagina1app/registro_y_adopcion.html")

def formulario_adopcion(request):
    return render(request,"pagina1app/formulario_adopcion.html")

def registro(request):
    return render(request, 'registration/registro.html')
