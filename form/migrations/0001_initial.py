# Generated by Django 2.0.5 on 2019-09-15 18:21

from django.db import migrations, models
import django.db.models.deletion
import form.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('celular', models.IntegerField()),
                ('correo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('monto', models.IntegerField()),
                ('tiempo', models.IntegerField()),
                ('mensualidad', models.IntegerField()),
                ('dia', models.CharField(default='2019/09/15', max_length=50)),
                ('hora_registro', models.CharField(default=form.models.get_default_my_hour, max_length=50)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.Productos')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='item_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='form.Solicitud'),
        ),
    ]
