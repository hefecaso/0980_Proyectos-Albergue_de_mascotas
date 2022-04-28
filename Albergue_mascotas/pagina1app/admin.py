from django.contrib import admin
from .models import Contacto, Registro_mascota, Solicitud_adopcion
from django.contrib.auth.models import Group


#class PuppyHeroeAdmin(admin.ModelAdmin):
    #exclude = ('title',)
    #fields = ('title',)
    #list_display = ('title', 'created')
    #list_filter = ('created')
        #No funcionó o no entendí XD
    #change_list_template = 'admin/puppy_heroe_admin/admin_dashboard.html'

# Register your models here.

admin.site.register(Contacto)
admin.site.register(Registro_mascota)
admin.site.register(Solicitud_adopcion)

#Con unregister desaparecemos un campo en el admin
admin.site.unregister(Group)
#admin.site.unregister(Temas)

#Cambiando título de Djadmin
admin.site.site_header = "Puppy Heroe - Admin dashboard"
