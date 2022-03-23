from django.http import HttpResponse

#def hola_mundo(request): #Primera vista
    #return HttpResponse("Hola mundo!")

def index(request):
    template_name = "index.html"
    return render(request,template_name)
