# Generated by Django 5.1.4 on 2024-12-16 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universo', '0010_alter_persona_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='ahorros',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
    ]
