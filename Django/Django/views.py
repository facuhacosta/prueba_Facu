from os import read
from django.http import HttpResponse
import datetime
from django.template import Template, Context 
from django.template.loader import get_template 
from django.shortcuts import render

def saludo(request):
    nombre= "juan"
    apellido= "Nuss"
    ahora=datetime.datetime.now
    #a=open ("C:/Users/nusss/Desktop/Django/Django/Plantillas/plantilla.html")
    #tmp=Template(a.read())
    #a.close()
    #ctx=Context({'nombre_persona': nombre,'apellido_persona':apellido, 'ahora':ahora})
    #documento=tmp.render(ctx)
    return render(request, 'plantilla.html',{'nombre_persona': nombre,'apellido_persona':apellido, 'ahora':ahora})

def damefecha(request, agno, edad):
    fecha_actual=datetime.datetime.now()
    edad_actual=edad
    diferencia= edad_actual+(agno - 2021)

    return HttpResponse("En el año %s vas a tenr %s" %(agno, diferencia))

def curso (request):
    return render(request, 'cursoC.html')
    