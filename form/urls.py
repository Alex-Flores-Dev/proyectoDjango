from django.urls import path,include
from django.conf.urls import url
from form import views

##from form.view import evaluacion



urlpatterns = [
    url(r'^(?P<index>\w+)/$',views.index,name='index'),
    url(r'^nuevo$' ,views.vista_formulario.as_view(),name='formulario'),
]
