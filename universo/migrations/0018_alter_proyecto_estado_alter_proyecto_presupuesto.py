# Generated by Django 5.1.4 on 2024-12-18 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universo', '0017_rename_persona_proyecto_responsable_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='estado',
            field=models.TextField(choices=[('En proceso', 'En proceso'), ('Finalizado', 'Finalizado'), ('Cancelado', 'Cancelado')], max_length=20),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='presupuesto',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
