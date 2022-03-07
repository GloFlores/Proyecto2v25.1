from django import forms

class Formulario (forms.Form):
    nombre=forms.CharField(max_length=100)
    numero_documento= forms.CharField(max_length=10)
    correo_electronico= forms.EmailField()
    