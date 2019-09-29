from django.db import models
from django.utils import timezone

# Create your models here.
class Productos(models.Model):
    producto=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.producto)

def get_default_my_hour():
    hour=timezone.now()
    formatedHour=hour.strftime("%H:%M:%S")
    return formatedHour


class Solicitud(models.Model):
    day=timezone.now()
    formatedDay=day.strftime("%Y/%m/%d")

    item_id=models.AutoField(primary_key=True)
    monto=models.IntegerField()
    tiempo=models.IntegerField()
    mensualidad=models.IntegerField()
    dia=models.CharField(max_length=50,default=formatedDay)
    hora_registro=models.CharField(max_length=50,default=get_default_my_hour)
    producto=models.ForeignKey(Productos,null=False,on_delete=models.CASCADE)

    def get_all_objects(self):
        queryset=self._meta.models.objects.all()
        return queryset

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    celular=models.IntegerField()
    correo=models.CharField(max_length=50)
    item_id=models.ForeignKey(Solicitud,null=True,blank=True,on_delete=models.CASCADE)

class Bancos(models.Model):
    banco=models.CharField(max_length=50)
    tipo_producto=models.CharField(max_length=50)
    moneda=models.CharField(max_length=10)
    plazo=models.IntegerField()
    interes=models.FloatField()
    def get_all_objects(self):
        consulta_banco=self._meta.models.objects.all()
        return consulta_banco
