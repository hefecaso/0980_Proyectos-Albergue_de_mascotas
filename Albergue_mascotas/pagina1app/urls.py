from django.urls import path, include
#importamos de la primer app lo relacionado
#a las vistas
from pagina1app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.contrib.auth import views as auth_views #Password reset

urlpatterns = [

    path('',views.home, name="Home"),
    path('servicios/',views.servicios, name="Servicios"),
    path('albergue/',views.albergue, name="Albergue"),
    #path('iniciosesion',views.iniciosesion, name="Inicio de sesión"),
    path('contacto/',views.contacto, name="Contacto"),
    path('registro_y_adopcion/',views.registro_y_adopcion, name="Formularios registro y adopcion"),
    path('formulario_registro_mascota/',views.formulario_registro_mascota, name="Formulario registro"),
    path('formulario_adopcion/',views.formulario_adopcion, name="Formulario adopcion"),
    path('registro/',views.registro, name="Formulario Registro"),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name = "Reset password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name = "Password reset done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name = "Password reset confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name = "Password reset complete"),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


'''
1 - Submit email form                           //PasswordResetView.as_view()
2 - Email sent succes massage                   //PasswordResetDoneView.as_view()
3 - Link to password Reset form in email        //PasswordResetConfirmView.as_view()
4 - Password succesfully changed message        //PasswordResetCompleteVies.as_view()
'''
