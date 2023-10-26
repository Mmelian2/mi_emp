# Generated by Django 4.2.5 on 2023-09-17 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='domicilio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prov', models.CharField(max_length=50, verbose_name='Provincia')),
                ('pais', models.CharField(max_length=50, verbose_name='País')),
                ('calle', models.CharField(max_length=50, verbose_name='Calle')),
                ('numero', models.CharField(max_length=10, verbose_name='Número')),
            ],
        ),
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('dni', models.CharField(max_length=8, verbose_name='DNI')),
                ('email', models.EmailField(default='ejemplo@gmail.com', max_length=250, unique=True)),
                ('rubro', models.CharField(max_length=50, verbose_name='Rubro')),
                ('dom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clientes.domicilio')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
