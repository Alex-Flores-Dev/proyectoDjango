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
