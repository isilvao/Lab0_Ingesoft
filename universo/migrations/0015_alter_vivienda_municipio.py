# Generated by Django 5.1.4 on 2024-12-18 00:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universo', '0014_alter_vivienda_propietario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vivienda',
            name='municipio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='universo.municipio'),
        ),
    ]
