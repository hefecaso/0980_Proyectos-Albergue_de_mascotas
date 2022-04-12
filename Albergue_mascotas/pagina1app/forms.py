from  django import forms
from django.contrib.auth.forms import  UserCreationForm
from .models import Contacto, Registro_mascota

class CustomUserCreationForm(UserCreationForm):
    pass

class ContactoForm(forms.ModelForm):
    #Tomamos datos desde el modelo definido en models
    class Meta:
        model = Contacto
        #Asegurarse que los siguientes campos estén en el modelo, aparecera en el orden escrito
        fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        #Otra opción, para que aparezca en el orden que tiene en modelo.py podríamos escribir lo siguiente:
        #fields = '__all__'

class Registro_mascota_Form(forms.ModelForm):
    #Tomamos datos desde el modelo definido en models
    class Meta:
        model = Registro_mascota
        #Asegurarse que los siguientes campos estén en el modelo, aparecera en el orden escrito
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        #Otra opción, para que aparezca en el orden que tiene en modelo.py podríamos escribir lo siguiente:
        fields = '__all__'

        labels ={
            'id_mascota': 'ID de la mascota',
            'nombre_mascota': 'Nombre de la mascota',
            'sexo_mascota': 'Sexo de la mascota',
            'edad_mascota': 'Edad de la mascota',
            'fecha_rescate_mascota': 'Fecha de rescate (DD/MM/AAAA)',
            'fecha_vacuna_mascota': 'Fecha de vacunación',
            'foto_mascota': 'Foto de la mascota',
            'raza_mascota': 'Raza de la mascota',
            'vacunas_mascota': 'Vacunas de la mascota',
        }





'''
Referencias:
https://www.youtube.com/watch?v=90M4gunBRLs&t=174s&ab_channel=moisessepulveda
'''
