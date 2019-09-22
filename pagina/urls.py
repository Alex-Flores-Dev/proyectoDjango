from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

##from form.view import evaluacion



urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^formulario/',include(('form.urls','formularios'), namespace='formularios')),
]
