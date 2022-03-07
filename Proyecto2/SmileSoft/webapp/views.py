from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect, request
from webapp.forms import Formulario
from django.http import (
    Http404, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect,
)
def registro(request):
   '''
    if request.method=='POST': 
        form= Formulario(request.POST)
        if form.is_valid():
            return HttpResponseRedirect ('/smilesoft/Consultorio/Sistema/Gracias/')
    else:
        form= Formulario()
   '''
   return render(request,"registro.html",{
        'form': Formulario(),
    })


