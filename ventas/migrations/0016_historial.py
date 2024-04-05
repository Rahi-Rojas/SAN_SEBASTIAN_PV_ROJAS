# Generated by Django 5.0.3 on 2024-04-05 03:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0015_remove_venta_productos_factura_lista_productos_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='historial',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.venta_productos_factura')),
            ],
        ),
    ]
