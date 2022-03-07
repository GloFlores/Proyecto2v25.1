#from _typeshed import Self
from re import VERBOSE
from typing import Match
from django import forms
from django.contrib import messages
from django.http import request
from .models import *
from webapp.models import *
#from django.core.mail import EmailMessage

class PersonaForm(forms.ModelForm):
   nombre= forms.CharField( widget = forms.TextInput (attrs = {'class': 'form-control', 'placeholder': 'Ingrese su nombre'}))
   apellido= forms.CharField( widget = forms.TextInput (attrs = {'class': 'form-control', 'placeholder': 'Ingrese su apellido'}))
   numero_documento= forms.CharField( widget = forms.TextInput (attrs = {'class': 'form-control', 'placeholder': 'Ingrese su documento'}))
   direccion = forms.CharField( widget = forms.TextInput (attrs = {'class': 'form-control', 'placeholder': 'Ingrese su dirección'}))
   telefono = forms.CharField( widget = forms.TextInput (attrs = {'class': 'form-control', 'placeholder': 'Ingrese su numero de telefono'}))
   correo_electronico = forms.EmailField( widget = forms.EmailInput (attrs = {'class': 'form-control', 'placeholder': 'Ingrese su correo electronico'}))
   fecha_nacimiento = forms.DateField( widget = forms.DateInput (attrs = {'class': 'form-control', 'placeholder': 'Ingrese su fecha de nacimiento'}))
   # sexo = forms.ChoiceField( widget = forms.cho(attrs = {'class': 'form-control', 'placeholder': 'Ingrese su documento'}))

   class Meta:
        model = Persona
        fields = ['nombre', 
                    'apellido', 
                     'numero_documento', 
                    'direccion',
                    'telefono',
                    'correo_electronico',
                    'fecha_nacimiento',
                    'sexo',
                    'es_funcionario',
                    'es_personal_salud',
                    'es_paciente',
                    'es_proveedor',
                ]
   def clean_numero_documento(self):
      numero_documento= self.cleaned_data["numero_documento"]
      if Persona.objects.filter(numero_documento=numero_documento).exists():
         print ("Ya existe el numero de cedula ingresado")
         #messages.error(request, 'Ya existe el numero de cedula ingresado')
            # self.error_cedula()
      return numero_documento
    
    # def error_cedula(self):
    #     respuesta =request.HttpRequest()
    #     messages.error(respuesta, "Ya existe el numero de cedula ingresado" )      
'''
    def validateEmail(email):
        if len(email) > 6:
            if Match('\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', email) != None:
                return 1
                #print ("CORREO VALIDO")
        return 0
        #print ("CORREO VALIDO")
'''

class FuncionarioForm(forms.ModelForm):
   #cargos= forms.MultiValueField( widget = forms.TextInput (attrs = {'class': 'form-control', 'placeholder': 'Ingrese su nombre'}))
   class Meta:
      model = Funcionario
      fields = ['numero_documento',
               'cargos',
                ]

class EspecialistaSaludForm(forms.ModelForm):
   es_interno= forms.ChoiceField( widget = forms.CheckboxInput (attrs = {'class': 'form-control', 'placeholder': 'Ingrese su nombre'}))
   es_externo= forms.ChoiceField( widget = forms.CheckboxInput (attrs = {'class': 'form-control', 'placeholder': 'Ingrese su nombre'}))
   class Meta:
      model = EspecialistaSalud
      fields = [    'es_interno',
                    'es_externo',
                  #  'TrabajosRealizados',
                ]

class PacienteForm(forms.ModelForm):
     class Meta:
        model = Paciente
        fields = ['numero_documento',
                ]

class EmpleadoPacienteForm(forms.ModelForm):
     class Meta:
        model = Funcionario # and Paciente
        fields = ['numero_documento',
                  'cargos',
                ]