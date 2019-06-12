from django.db import models
from django.conf import settings


#TIPIFICACIONES---------------------------------------------------
#TIPIFICACIONES---------------------------------------------------
#TIPIFICACIONES---------------------------------------------------
class Criticidad(models.Model):
	nombre = models.CharField(max_length = 40)

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name = "criticidad"
		verbose_name_plural = "criticidades"

class TipoSolicitud(models.Model):
	nombre = models.CharField(max_length = 40)

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name = "tipo de solicitud"
		verbose_name_plural = "tipos de solicitud"


#TIPIFICACIONES---------------------------------------------------
#TIPIFICACIONES---------------------------------------------------
#TIPIFICACIONES---------------------------------------------------



class Proyecto(models.Model):
	nombre = models.CharField(max_length = 40)

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name = "proyecto"
		verbose_name_plural = "proyectos"

class Cliente(models.Model):
	usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	proyecto = models.ForeignKey(Proyecto, on_delete = models.CASCADE)
	
	class Meta:
		verbose_name = "cliente"
		verbose_name_plural = "clientes"

	def __str__(self):
		return str(self.usuario)

class SolicitudMantenimiento(models.Model):
	proyecto = models.ForeignKey(Proyecto, on_delete = models.CASCADE)

	nombre = models.CharField(max_length = 70)
	#fechaCreacion = models.DateField(null = True, blank = True)
	fechaNecesidad = models.DateField(null = True, blank = True)
	tipo = models.ForeignKey(TipoSolicitud, on_delete = models.SET_NULL,null = True)
	descripcion = models.CharField(max_length = 250)
	archivosAdjuntos = models.FileField(upload_to='adjuntos')
	criticidad = models.ForeignKey(Criticidad, on_delete = models.SET_NULL,null = True)
	#creador = models.ForeignKey(Cliente, on_delete = models.SET_NULL)


	class Meta:
		verbose_name = "solicitud de mantenimiento"
		verbose_name_plural = "solicitudes de mantenimiento"

	def __str__(self):
		return str(self.nombre)

