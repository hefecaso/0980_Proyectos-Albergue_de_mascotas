from django.http import HttpResponse

def hola_mundo(request): #Primera vista
    return HttpResponse("Hola mundo!")
