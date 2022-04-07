from django.urls import path
#importamos de la primer app lo relacionado
#a las vistas
from pagina1app import views


urlpatterns = [

    path('',views.home, name="Home"),
    path('servicios',views.servicios, name="Servicios"),
    path('albergue',views.albergue, name="Albergue"),
    path('iniciosesion',views.iniciosesion, name="Inicio de sesión"),
    path('contacto',views.contacto, name="Contacto"),
    path('registro_y_adopcion',views.registro_y_adopcion, name="Formularios registro y adopcion"),
    path('formulario_registro_mascota',views.formulario_registro_mascota, name="Formulario registro"),
]
