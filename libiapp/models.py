from django.db import models

# Create your models here.

# Modelo Provincia

class Provincia(models.Model):
    """
    Modelo que representa a las Provincias
    """
    cprovincia = models.CharField(max_length=2,verbose_name="Código de Provincia", help_text="")
    nombreprovinciacastellano = models.CharField(max_length=100,verbose_name="Nombre en castellano")
    nombreprovincialenguaoficial = models.CharField(max_length=100,verbose_name="Nombre en la lengua oficial")
    

    def __str__(self):
        """
        Cadena que representa a la instancia en particular
        """
        return (self.nombreprovinciacastellano)


class Municipio(models.Model):
    """
    Modelo que representa a los Municipios
    """
    cprovincia = models.ForeignKey('Provincia',on_delete=models.SET_NULL,null=True,verbose_name="Provincia")
    cmunicipio = models.CharField(primary_key=True,max_length=5,verbose_name="Código de Municipio",help_text="")
    nombremunicipiocastellano = models.CharField(max_length=100,verbose_name="Nombre en castellano")
    nombremunicipiolenguaoficial = models.CharField(max_length=100,verbose_name="Nombre en la lengua oficial")

    def __str__(self):
        """
        Cadena que representa a la instancia en particular
        """
        return (self.nombremunicipiocastellano + " / " + self.nombremunicipiolenguaoficial)


import uuid #Requerida para las claves primarias
from datetime import date
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Socio(models.Model):
    """
    Modelo que representa a los Socios
    """
    numero = models.IntegerField(primary_key=True,default=0, verbose_name="Número")
    nombre = models.CharField(max_length=100,verbose_name="Nombre")
    apellidos = models.CharField(max_length=100,verbose_name="Apellidos")
    nif_nie = models.CharField(blank=True,max_length=9,verbose_name="NIF/NIE")
    domicilio = models.CharField(blank=True,max_length=100,verbose_name="Domicilio")
    cpostal = models.CharField(blank=True,max_length=5,verbose_name="Código Postal")
    cprovincia = models.ForeignKey('Provincia',on_delete=models.SET_NULL,null=True,verbose_name="Provincia")
    cmunicipio = models.ForeignKey('Municipio',on_delete=models.SET_NULL,null=True,verbose_name="Municipio")
    fecha_alta = models.DateField(null=False,blank=False,default=date.today)
    fecha_baja = models.DateField(null=True,blank=True)
    cuota = models.DecimalField(max_digits=5,decimal_places=2,default=7.00,verbose_name="Cuota")
    
    LOAN_PERIODO = (
        ('0','Mensual'),
        ('1','Trimestral'),
        ('2','Semestral'),
        ('3','Anual'),
    )
    periodo = models.CharField(max_length=1,choices=LOAN_PERIODO,default="0",verbose_name="Periodo")

    def __str__(self):
        """
        Cadena que representa a la instancia en particular
        """
#       return (str(self.numero) + " - " + self.apellidos + ", " + self.nombre + " / " + self.nif_nie)
        return '%s (%s)' % (self.numero,self.apellidos)

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Socio
        """
        return reverse('socio-detail', args=[str(self.numero)])

    class Meta:
        ordering=["numero"]
        permissions = (("can_mark_returned", "Set book as returned"),)

class Incidencia(models.Model):
    """
    Modelo que representa a las Incidencias
    """
    numero = models.ForeignKey('Socio',on_delete=models.SET_NULL,null=True)
    fecha = models.DateField(null=False)
    descripcion = models.TextField(blank=True,max_length=300,verbose_name="Descripción")

    LOAN_ESTADO = (
        ('a','Abierta'),
        ('e','En curso'),
        ('c','Cerrada'),
    )
    estado = models.CharField(max_length=1,choices=LOAN_ESTADO,blank=True,default='m',verbose_name="Estado")
    observaciones = models.TextField(blank=True,max_length=300,verbose_name="Observaciones")

    def __str__(self):
        """
        Cadena que representa a la instancia en particular
        """
        return '%s (%s)' % (self.id,self.numero)

class ReciboDevuelto(models.Model):
    """
    Modelo que representa a los Recibos Devueltos
    """
    numero = models.ForeignKey('Socio',on_delete=models.SET_NULL,null=True)
    fecha = models.DateField(null=False)
    referencia = models.CharField(max_length=35,verbose_name="Referencia")
    importe = models.DecimalField(max_digits=5,decimal_places=2,default=7.00,verbose_name="Importe")
    titular = models.CharField(max_length=100,verbose_name="Titular Domiciliación")
    iban = models.CharField(max_length=24,verbose_name="IBAN")

    LOAN_MOTIVO = (
        ('AC01','Número de IBAN incorrecto'),
        ('AC04','Número de cuenta cancelada'),
        ('AC06','Cuenta bloqueada'),
    )
    motivo = models.CharField(max_length=4,choices=LOAN_MOTIVO,verbose_name="Motivo")
    observaciones = models.TextField(blank=True,max_length=300,verbose_name="Observaciones")#

    def __str__(self):
        """
        Cadena que representa a la instancia en particular
        """
        return '%s (%s)' % (self.id,self.Socio.apellidos)