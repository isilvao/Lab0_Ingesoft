# Generated by Django 5.1.4 on 2024-12-16 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universo', '0008_alter_persona_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]