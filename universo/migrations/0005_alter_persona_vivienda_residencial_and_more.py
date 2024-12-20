# Generated by Django 5.1.4 on 2024-12-15 03:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universo', '0004_alter_municipio_area_alter_persona_ahorros_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='vivienda_residencial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universo.vivienda'),
        ),
        migrations.AlterField(
            model_name='vivienda',
            name='propietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universo.persona'),
        ),
    ]
