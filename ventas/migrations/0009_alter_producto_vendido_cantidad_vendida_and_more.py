# Generated by Django 5.0.3 on 2024-03-23 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0008_producto_vendido_codigo_venta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto_vendido',
            name='cantidad_vendida',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='producto_vendido',
            name='codigo_venta',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
