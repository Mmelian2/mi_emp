# Generated by Django 4.2.5 on 2023-10-07 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_remove_cliente_dom_remove_empresa_dom_cliente_calle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='foto',
            field=models.ImageField(blank=True, max_length=254, null=True, upload_to='cliente/', verbose_name='Foto 4x4'),
        ),
    ]
