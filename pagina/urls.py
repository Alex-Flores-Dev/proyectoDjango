from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from form import views,calculos

##from form.view import evaluacion



urlpatterns = [
    url(r'^registro$' ,views.vista_formulario,name='registro'),
    url(r'^admin/',admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^evaluacion/$',calculos.calculo,name='evaluacion'),
    url(r'^cliente/$',views.cliente_formulario,name='cliente'),



]
