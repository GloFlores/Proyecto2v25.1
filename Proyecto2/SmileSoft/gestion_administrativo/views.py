from django.shortcuts import redirect, render
from .forms import *
from django.contrib import messages

# Create your views here

def crear_persona(request):
    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():
            content = form.save()
            if content.es_funcionario is True:
                return redirect('add_empleado/', key=content.numero_documento)
            else:
                if content.es_personal_salud is True:
                    return redirect('add_tercerizado/', key=content.numero_documento)
                else:
                    if content.es_paciente is True:
                        return redirect('add_paciente/', key=content.numero_documento)
        else:
            messages.error(request, 'Ya existe el numero de cedula ingresado')      
    form = PersonaForm()
    return render(request, 'registro_de_datos.html', {'form': form})


def crear_funcionario(request):
    if request.method == "POST":
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            content = form.save()
            return redirect('/gestion_administrativo/persona/', key=content.numero_documento)
    form = FuncionarioForm()
    return render(request, 'agregar_funcionario.html', {'form': form})

def crear_especialista_salud(request):
    if request.method == "POST":
        form = EspecialistaSaludForm(request.POST)
        if form.is_valid():
            content = form.save()
            return redirect('/gestion_administrativo/especialistasalud/', key=content.numero_documento)
    form = EspecialistaSaludForm()
    return render(request, 'agregar_especialista_salud.html', {'form': form})

def crear_paciente(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            content = form.save()
            return redirect('/gestion_administrativo/paciente/', key=content.numero_documento)
    form = PacienteForm()
    return render(request, 'agregar_paciente.html', {'form': form})

def crear_empleado_paciente(request):
    if request.method == "POST":
        form = EmpleadoPacienteForm(request.POST)
        if form.is_valid():
            content = form.save()
            return redirect('/gestion_administrativo/paciente/', key=content.numero_documento)
    form = EmpleadoPacienteForm()
    return render(request, 'agregar_paciente.html', {'form': form})

