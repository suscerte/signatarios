from django.db import models
from proveedores.models import Proveedor

class Certificado(models.Model):
	signatario_id = models.ForeignKey("Signatario")
	serial = models.IntegerField(help_text='Serial unico del certificado')
	estado_id = models.ForeignKey("Estado")
	fecha_emision = models.DateField()
	fecha_revocacion = models.DateField()
	tipo = models.CharField(max_length = 1024)
	proveedor_id = models.ForeignKey(Proveedor)

	def __unicode__(self):
		return self.serial

class Signatario(models.Model):
	nombres = models.CharField(max_length = 1024)
	ip = models.CharField(max_length = 15)
	correo = models.CharField(max_length = 100)

	def __unicode__(self):
		return self.nombres

class Estado(models.Model):
	nombre = models.CharField(max_length = 1024)

	def __unicode__(self):
		return self.nombre
