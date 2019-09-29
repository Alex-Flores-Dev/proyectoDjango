from django.shortcuts import render, redirect
from form.formulario import FormularioDeSolicitud,FormularioCliente
from django.http import HttpResponse
from django.views.generic import ListView,CreateView
from form.models import Solicitud
from django.urls import reverse_lazy
from pagina import views
from form.calculos import calculo

def index(request):
##    respuesta=Solicitud.objects.last()
##    respuestas_string='<br/>'.join([(form.monto) for form in solicitud])
##    return HttpResponse(respuesta.tiempo)
    return render(request, 'formularios/index.html')

"""class vista_formulario(CreateView):
    model=Solicitud
    form_class=FormularioDeSolicitud
    template_name='formularios/credito.html'
    success_url=reverse_lazy('formularios:index')"""

"""PARA LA SOLICITUD"""


def vista_formulario(request):
    if request.method=='POST':
        form=FormularioDeSolicitud(request.POST)
        if form.is_valid():
            form.save()
        return redirect('evaluacion')
    else:
        form=FormularioDeSolicitud()

    return render(request,'formularios/credito.html',{'form':form})


"""PARA EL CLIENTE"""


def cliente_formulario(request):
    if request.method=='POST':
        cliente=FormularioCliente(request.POST)
        if cliente.is_valid():
            cliente.save()
        return redirect('index')
    else:
        cliente=FormularioCliente()

    return render(request,'formularios/cliente.html',{'cliente':cliente})



class evaluacion(ListView):
    model=Solicitud
    template_name='formularios/evaluacion.html'
