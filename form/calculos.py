from django.shortcuts import render, redirect
from form.formulario import FormularioDeSolicitud
from django.http import HttpResponse
from django.views.generic import ListView,CreateView
from form.models import Solicitud,Cliente,Productos,Bancos
from django.urls import reverse_lazy
from pagina import views




def calculo(request):
    datos=Solicitud.objects.last()
    monto=datos.monto
    tiempo=datos.tiempo
    tiempo_efectivo=tiempo

    """ EL IF ES PARA CONDICIONAR SI EL PRODUCTO ES DPF O CCA"""
    if str(datos.producto)=="Deposito a Plazo Fijo":
        if tiempo_efectivo<60:
            tiempo_efectivo=30
        elif tiempo_efectivo>=60 and tiempo<90:
            tiempo_efectivo=60
        elif tiempo_efectivo>=90 and tiempo<180:
            tiempo_efectivo=90
        elif tiempo_efectivo>=180 and tiempo<360:
            tiempo_efectivo=180
        elif tiempo_efectivo>=360 and tiempo<720:
            tiempo_efectivo=360
        elif tiempo_efectivo>=720 and tiempo<1080:
            tiempo_efectivo=720
        elif tiempo_efectivo>=1080:
            tiempo_efectivo=1080

        listado=Bancos.objects.filter(plazo=tiempo_efectivo).values('banco','interes')
        resultado=[]
        for interes in listado:
            informe=round(interes['interes']*monto+monto,2)
            diferencia=round(informe-monto,2);

            resultado.append({"banco":interes['banco'],"ahorros":informe,"tiempo":datos.tiempo,"diferencia":diferencia,"producto":1})

## EL ELSE ES PARA EVALUAR LA CCA

    else:
        listado=Bancos.objects.filter(plazo=1).values('banco','interes')
        resultado=[]
        """ FOR PARA RECORRER EL OBJETO """
        for interes in listado:
            """PARA EL INTERES POR MES """
            interes_capitalizable=interes['interes']/12
            if (tiempo/30)>0:
                multiplicador=int(tiempo/30)
                interes_capitalizable=interes_capitalizable*multiplicador
                informe=round(interes_capitalizable*monto+monto,2)
                diferencia=round(informe-monto,2);
                resultado.append({"banco":interes['banco'],"ahorros":informe,"tiempo":datos.tiempo,"diferencia":diferencia,"producto":0})
            else:
                informe=monto
                diferencia=round(informe-monto,2)
                resultado.append({"banco":interes['banco'],"ahorros":informe,"tiempo":datos.tiempo,"diferencia":diferencia,"producto":0})

    ##    solicitud=Solicitud.objects.all()
    ##    respuestas_string="Solicitud <br/>"
    ##    respuestas_string='<br/>'.join([(form.monto) for form in solicitud])
    return render(request,'formularios/evaluacion.html',{'resultado':resultado})
