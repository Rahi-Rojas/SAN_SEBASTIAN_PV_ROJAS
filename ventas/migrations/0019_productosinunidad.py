# Generated by Django 5.0.3 on 2024-04-09 13:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0018_historial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoSinUnidad',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('codigo_producto', models.CharField(max_length=20, unique=True)),
                ('codigo_barras', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=255)),
                ('precio_por_kilo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock_en_gramos', models.PositiveIntegerField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos/')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.categoria')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.marca')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.proveedor')),
            ],
        ),
    ]
