# Generated by Django 5.0.3 on 2024-04-13 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0022_alter_lista_productosinunidad_factura_cantidad_vendida_gramos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lista_productosinunidad_factura',
            name='cantidad_vendida_gramos',
            field=models.DecimalField(decimal_places=5, max_digits=15),
        ),
    ]