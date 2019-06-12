import os
import django
import sys
os.environ['DJANGO_SETTINGS_MODULE'] = "poloc.settings"
django.setup()
from django.contrib.auth.models import User
sys.path.append('poloc')

from polocApp.models import *


Proyecto.objects.all().delete()
Criticidad.objects.all().delete()
TipoSolicitud.objects.all().delete()

criticidades=[
	"Crítico",
	"Bloqueante",
	"Medio", 
	"Deseado"
]
criticidadesObj=[]

tipoSol=[
	"Nuevo requerimiento",
	"Correctivo",
	"Cambio"
]
tipoSolObj=[]



proyectos=[
	"Software 1",
	"Software 2"
]
proyectosObj=[]



for criticidad in criticidades:
	c=Criticidad(nombre=criticidad)
	c.save()
	criticidadesObj.append(c)

for tiposolicitud in tipoSol:
	t=TipoSolicitud(nombre=tiposolicitud)
	t.save()
	tipoSolObj.append(t)

for proyecto in proyectos:
	p=Proyecto(nombre=proyecto)
	p.save()
	proyectosObj.append(p)