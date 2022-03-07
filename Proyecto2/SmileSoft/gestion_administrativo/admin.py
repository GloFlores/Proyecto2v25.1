from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.

class AdminPersona(admin.ModelAdmin):
    #add_form_template = PersonForm
    fieldsets = (
        (None, {'fields': (
                            'numero_documento',)}),
        (('Informacion Personal'), {'fields': (
                                            'nombre', 
                                            'apellido', 
                                            'correo_electronico', 
                                            'direccion', 
                                            'telefono',
                                        )
                                    }
        ),
        (('Rol en el sistema'), {'fields': (
                                            'es_funcionario',
                                            'es_personal_salud',
                                            'es_paciente',
                                            'es_proveedor',
                                        )
                                    }
        ), 
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nombre', 'apellido',),
        }),
    )

    list_display = ['numero_documento',"nombre", "apellido",]
    # list_filter = ['numero_documento']
    search_fields = ["numero_documento","nombre","apellido",]
    ordering = ["nombre","apellido",]
    # filter_horizontal = ('groups',)

class PersonalInternoCargoInline(admin.TabularInline):
    model = PersonalInternoCargo
    extra = 1
    # autocomplete_fields = ['cargo',]

class AdminPersonalInternoCargo(admin.ModelAdmin):
    inlines = [PersonalInternoCargoInline,]
    search_fields = ['cargo']
    ordering = ['cargo']

class AdminPersonalInterno(admin.ModelAdmin):
    inlines = [PersonalInternoCargoInline,]
    list_display = ["numero_documento"]

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('numero_documento',),
        }),
    )

    fieldsets = (
        (None, {'fields': ('numero_documento',)}),
    )

    filter_horizontal = ['cargos']

    # list_display = ["nombre", "apellido",]
    # list_filter = ['numero_documento']
    search_fields = ['numero_documento', ]
    ordering = ['numero_documento']

class PersonalTercerizadoEspInline(admin.TabularInline):
    model = TrabajoRealizado
    extra = 1
    #autocomplete_fields = ['especialidad',]

class AdminPersonalTercerizadoEsp(admin.ModelAdmin):
    inlines = [PersonalTercerizadoEspInline,]
    search_fields = ['especialidad']
    ordering = ['especialidad']


class AdminPersonalTercerizado(admin.ModelAdmin):
    inlines = [PersonalTercerizadoEspInline,]
    fieldsets = (
        (None, {'fields': ('numero_documento',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('numero_documento',),
        }),
    )
    # list_display = ["nombre", "apellido",]
    # list_filter = ['numero_documento']
    search_fields = ['numero_documento',]
    ordering = ['numero_documento']

class AdminProveedor(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('numero_documento',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('numero_documento',),
        }),
    )
    # list_display = ["nombre", "apellido",]
    # list_filter = ['numero_documento']
    search_fields = ['numero_documento',]
    ordering = ['numero_documento']

class TratamientoRealizadoInline(admin.TabularInline):
    model = TratamientoRealizado
    extra = 1
    # autocomplete_fields = ['cargo',]

class AdminTratamientoRealizado(admin.ModelAdmin):
    #inlines = [TratamientoRealizadoInline,]
    search_fields = ['codigo_tratamiento']
    ordering = ['codigo_tratamiento']

class AdminPaciente(admin.ModelAdmin):
    #inlines = [TratamientoRealizadoInline,]
    # list_filter = ('numero_documento',)
    fieldsets = (
        (None, {'fields': (
                            'numero_documento', 
                            'numero_ficha', 
                            'grupo_sanguineo',
                            )}),
        (('Antecedente Clínico'), {'fields': (
                                            'enfermedad_base', 
                                            'alergia', 
                                            'tolerancia_anestecia', 
                                            'frecuencia_higiene_bucal',
                                            'cirugias',
                                            'afecciones_graves',
                                            'afeccion_cronica_familiar',
                                            'medicamento',
                                            'caries',
                                        )
                                    }
        ),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('numero_documento','numero_ficha'),
        }),
    )

    # list_display = ["nombre", "apellido",]
    # list_filter = ['numero_documento']
    search_fields = ['numero_documento',]
    ordering = ['numero_documento']

admin.site.site_header = 'Bienvenido a Smilesoft'
admin.site.site_title = 'SmileSoft'

admin.site.register(Persona, AdminPersona)
# admin.site.register(Cargo, AdminPersonalInternoCargo)
# admin.site.register(Especialidad, AdminPersonalTercerizadoEsp)
admin.site.register(Funcionario, AdminPersonalInterno)
admin.site.register(Proveedor, AdminProveedor)
admin.site.register(Paciente, AdminPaciente)
admin.site.register(EspecialistaSalud, AdminPersonalTercerizado)
admin.site.register(Categoria)
