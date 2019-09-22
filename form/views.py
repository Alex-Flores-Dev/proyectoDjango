from django.shortcuts import render, redirect
from form.formulario import FormularioDeSolicitud
from django.http import HttpResponse
from django.views.generic import ListView,CreateView
from form.models import Solicitud
from django.urls import reverse_lazy
from pagina import views



def index(request):
    return render(request, 'formularios/index.html')

class vista_formulario(CreateView):
    model=Solicitud
    form_class=FormularioDeSolicitud
    template_name='formularios/credito.html'
    success_url=reverse_lazy('formularios:index')

"""def vista_formulario(request):
    if request.method=='POST':
        form=FormularioDeSolicitud(request.POST)
        if form.is_valid():
            form.save()
        return redirect('formularios:index')
    else:
        form=FormularioDeSolicitud()

    return render(request,'formularios/credito.html',{'form':form})"""

class evaluacion(ListView):
    model=Solicitud
    template_name='formularios/evaluacion.html'
