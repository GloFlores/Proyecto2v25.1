from django.db import models
from django.db.models.deletion import PROTECT
from django.template.defaultfilters import default
from gestion_historial_clinico.models import HistorialClinico
from agregar_mas.models import *
from gestion_tratamiento.models import Tratamiento

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=40, verbose_name='Nombre (*)')
    apellido = models.CharField(max_length=40,  verbose_name='Apellido (*)')
    numero_documento = models.CharField(primary_key=True, max_length=10, verbose_name='Cedula de identidad')
    direccion = models.CharField(max_length=40,  verbose_name='Dirección')
    telefono = models.CharField(max_length=20,  verbose_name='Telefono')
    # correo_electronico = models.CharField(max_length=35,  verbose_name='Correo electrónico')
    correo_electronico = models.CharField(max_length=35,  verbose_name='Correo electrónico')
    fecha_nacimiento = models.DateField(null=True,  verbose_name='Fecha de nacimiento')
    F = 'Femenino'
    M = 'Masculino'
    SEXOS = ((F, 'Femenino'), (M, 'Masculino'))
    sexo = models.CharField(max_length=12, choices=SEXOS, verbose_name='Sexo')
    es_funcionario = models.BooleanField(verbose_name='Funcionario', default=False)
    es_personal_salud = models.BooleanField(verbose_name='Personal de salud', default=False)
    es_paciente =models.BooleanField(verbose_name='Paciente', default=False)
    es_proveedor = models.BooleanField(verbose_name='Proveedor', default=False)

    class Meta:
        # ordering = ['nombre']
        verbose_name_plural = 'Registro de personas'
        db_table = 'Persona'

    def __str__(self):
        # return self.numero_documento
        return self.nombre+' '+self.apellido+'    CI: '+self.numero_documento


class Funcionario(models.Model):
    numero_documento = models.OneToOneField(
                                                Persona, 
                                                max_length=10, 
                                                null=False, 
                                                blank= False, 
                                                primary_key=True, 
                                                on_delete=models.PROTECT,
                                                # verbose_name='Cedula de identidad'
                                            )
    cargos = models.ManyToManyField(Cargo, through='PersonalInternoCargo')

    class Meta:
        # ordering = ['nombre']
        verbose_name_plural = 'Funcionarios'
        db_table = 'Funcionario'

    def __str__(self):
        return str(self.numero_documento)

class PersonalInternoCargo(models.Model):
    personal_interno = models.ForeignKey(
        Funcionario, 
        on_delete=models.PROTECT, 
        blank=True, null=True
    )

    cargo= models.ForeignKey(
        Cargo,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )

    salario = models.BigIntegerField(null=True)
    class Meta:
        db_table = 'PersonalInternoCargo'
        verbose_name = 'Cargo de empleado'
        verbose_name = 'Cargos de empleado'

class Categoria(models.Model):
    codigo_categoria= models.AutoField(primary_key=True, verbose_name='codigo')
    detalle_tratamiento= models.CharField(max_length=40, verbose_name='detalle')
    precio=models.IntegerField( verbose_name='Precio')
    codigo_tratamiento = models.ForeignKey(
                                            Tratamiento, 
                                            null=False, 
                                            blank=False, 
                                            on_delete=models.PROTECT,
                                            verbose_name='Código de tratamiento'
                                        )

    
    class Meta:
        verbose_name = ("Categoria")
        verbose_name_plural = ("Categorias")
        db_table = 'Categoria'

    def __str__(self):
        return self.detalle_tratamiento

class EspecialistaSalud(models.Model):
    numero_documento = models.OneToOneField(
                                                Persona, 
                                                max_length=10, 
                                                null=False, 
                                                blank= False, 
                                                primary_key=True, 
                                                on_delete=models.PROTECT,
                                                # verbose_name='Cedula de identidad'
                                            )
    es_interno = models.BooleanField(null=True, blank=True,verbose_name='Es interno' )
    es_externo = models.BooleanField(null=True, blank=True, verbose_name='Es externo')
    TrabajosRealizados = models.ManyToManyField(Categoria, through='TrabajoRealizado')

    class Meta:
        # ordering = ['nombre']
        verbose_name = 'Especialista de salud'
        verbose_name_plural = 'Especialistas de salud'
        db_table = 'EspecialistaSalud'

    def __str__(self):
        return str(self.numero_documento)

class TrabajoRealizado(models.Model):
    especialista_salud = models.ForeignKey(
        EspecialistaSalud, 
        on_delete=models.PROTECT, 
        blank=True, null=True
    )

    categoria= models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    ) 

    costo_servicio = models.BigIntegerField(null=True, verbose_name='Costo de servicio')
    class Meta:
        db_table = 'TrabajoRealizado'
        verbose_name = 'Trabajo Realizado'
        verbose_name_plural = 'Trabajos Realizados'

class Paciente(models.Model):
    numero_documento = models.OneToOneField(
                                            Persona, max_length=10, 
                                            null=False, 
                                            blank= False, 
                                            primary_key=True, 
                                            on_delete=models.PROTECT,
                                            # verbose_name='Numero de cedula'
                                        )
    #TratamientosRealizados = models.ManyToManyField(Tratamiento, through='TratamientoRealizado')
    numero_ficha = models.OneToOneField(HistorialClinico,verbose_name='Número de ficha',on_delete=models.PROTECT, default=0)
    enfermedad_base = models.CharField(max_length=60, verbose_name='Enfermedad de base (*)',default='')
    alergia = models.CharField(max_length=60,  verbose_name='Alergia (*)',default='')
    tolerancia_anestecia = models.BooleanField(verbose_name='Tolerancia a la anestecia', default=False)
    frecuencia_higiene_bucal = models.CharField(max_length=60,  verbose_name='Frecuencia de higiene bucal (*)',default='' )
    medicamento = models.CharField(max_length=60,  verbose_name='Medicamento/s (*)',default='')
    cirugias = models.BooleanField(default=False, verbose_name='Cirugías (*)')
    caries = models.BooleanField(default=False, verbose_name='Caries (*)')
    afeccion_cronica_familiar = models.CharField(max_length=500,  verbose_name='Afección crónica familiar (*)',default='')
    afecciones_graves = models.CharField(max_length=500,  verbose_name='Afecciones graves (*)',default='')
    grupo_sanguineo = models.CharField(max_length=100,  verbose_name='Grupo sanguíneo (*)',default='')
    
    class Meta:
        verbose_name = ("paciente")
        verbose_name_plural = ("pacientes")
        db_table = 'Paciente'

    def __str__(self):
        return str(self.numero_documento)

class TratamientoRealizado(models.Model):
    codigo_tratamiento = models.ForeignKey(
        Tratamiento, 
        on_delete=models.PROTECT, 
        blank=True, null=True
    )

    numero_documento= models.ForeignKey(
        Paciente,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    numero_ficha = models.ForeignKey(HistorialClinico,verbose_name='Número de ficha',on_delete=models.PROTECT, null= True)

class Proveedor(models.Model):
    numero_documento = models.OneToOneField(
                                                Persona, 
                                                max_length=10, 
                                                null=False, 
                                                blank= False, 
                                                primary_key=True, 
                                                on_delete=models.PROTECT,
                                                #verbose_name='Cedula de identidad'
                                            )
    # costo_servicio = models.IntegerField()

    class Meta:
        # ordering = ['nombre']
        verbose_name_plural = 'Proveedores'
        db_table = 'Proveedor'

    def __str__(self):
        return str(self.numero_documento)
 
class Servicio(models.Model):
    # analizar si costo_servicio = models.IntegerField() debe ir aqui 
    # o en una tabla intermedia
    pass