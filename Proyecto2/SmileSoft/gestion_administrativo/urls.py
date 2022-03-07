from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *

urlpatterns = [
            path('registro_personas', crear_persona),
            path('add_funcionario/', crear_funcionario),
            path('add_tercerizado/', crear_especialista_salud),
            path('add_paciente/', crear_paciente),
            path('add_empleado_paciente/', crear_empleado_paciente),
]