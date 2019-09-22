from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from form import views

##from form.view import evaluacion



urlpatterns = [
    url(r'^nuevo$' ,views.vista_formulario.as_view(),name='formulario'),
    url(r'^admin/',admin.site.urls),
    url(r'^$',views.index,name='index'),

]
