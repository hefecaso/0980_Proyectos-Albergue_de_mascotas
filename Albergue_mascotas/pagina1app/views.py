from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):

    return render(request, "pagina1app/home.html")

def servicios(request):

    return render(request, "pagina1app/servicios.html")

def albergue(request):

    return render(request, "pagina1app/albergue.html")

def iniciosesion(request):

    return render(request, "pagina1app/iniciosesion.html")

def contacto(request):

    return render(request, "pagina1app/contacto.html")
