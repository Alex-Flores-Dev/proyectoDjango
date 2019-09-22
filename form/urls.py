from django.urls import path,include
from django.conf.urls import url
from form import views

##from form.view import evaluacion



urlpatterns = [
    url(r'^formulario/',include(('form.urls','formularios'), namespace='formularios')),
##    url(r'^(?P<index>\w+)/$',views.index,name='index'),


]
