from  django import forms
from django.contrib.auth.forms import  UserCreationForm
from .models import Contacto

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











'''
Referencias:
https://www.youtube.com/watch?v=90M4gunBRLs&t=174s&ab_channel=moisessepulveda
'''
