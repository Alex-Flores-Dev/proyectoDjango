from django import forms
from form.models import Solicitud,Cliente,Productos


class FormularioDeSolicitud(forms.ModelForm):

    def __init__(self, *args , **kwargs):
        super(FormularioDeSolicitud, self).__init__(*args, **kwargs)
        self.fields['producto'].queryset=Productos.objects.filter(tipo='Ahorro')

    monto=forms.CharField(max_length=20,help_text="Registre el monto que ahorrara")
    tiempo=forms.CharField(max_length=20,help_text="Resgistre el tiempo en meses")
    mensualidad=forms.CharField(max_length=20,help_text="Registre la monto mensual de ahorro ")

    class Meta:
        model=Solicitud

        fields=[
            'monto',
            'tiempo',
            'mensualidad',
            'producto'
        ]

class FormularioCliente(forms.ModelForm):


    nombre=forms.CharField(max_length=20,help_text="Porfavor registra tu nombre")
    apellido=forms.CharField(max_length=20,help_text="Porfavor registra tu Apellido")
    celular=forms.CharField(max_length=20,help_text="Porfavor registra tu celular ")
    correo=forms.CharField(max_length=50,help_text="Porfavor registra tu correo")

    class Meta:
        model=Cliente

        fields=[
            'nombre',
            'apellido',
            'celular',
            'correo'
        ]
