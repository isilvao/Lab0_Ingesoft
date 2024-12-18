from django.db import models


class Persona(models.Model):
    choices_sexo = [
        ("H", "Hombre"),
        ("M", "Mujer"),
        ("O", "Otro"),
        ("N", "Prefiero no responder"),
    ]
    nombre = models.CharField(max_length=45)
    telefono = models.BigIntegerField(null=True, blank=True)
    edad = models.BigIntegerField()
    sexo = models.CharField(max_length=1, choices=choices_sexo)
    ahorros = models.DecimalField(
        null=True, blank=True, max_digits=15, decimal_places=2
    )
    vivienda_residencial = models.ForeignKey(
        "Vivienda", null=True, blank=True, on_delete=models.SET_NULL
    )
    cabeza_de_familia = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "PERSONA"


class Municipio(models.Model):
    nombre = models.CharField(max_length=45)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    presupuesto = models.DecimalField(max_digits=20, decimal_places=2)
    persona = models.ForeignKey(
        Persona, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "MUNICIPIO"


class Vivienda(models.Model):
    direccion = models.CharField(max_length=45)
    capacidad = models.BigIntegerField()
    niveles = models.BigIntegerField()
    area = models.DecimalField(max_digits=10, decimal_places=2)
    municipio = models.ForeignKey(
        Municipio, null=True, blank=True, on_delete=models.SET_NULL
    )
    propietario = models.ForeignKey(
        Persona, null=True, blank=True, on_delete=models.SET_NULL
    )

    class Meta:
        db_table = "VIVIENDA"


class Evento(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=200)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    aforo = models.BigIntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "EVENTO"


class MunicipioEvento(models.Model):
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, null=True)
    evento = models.ForeignKey(Evento, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "MUNICIPIO_has_EVENTO"


class PersonaEvento(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True)
    evento = models.ForeignKey(Evento, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "PERSONA_goes_EVENTO"


class Proyecto(models.Model):

    state_choices = [
        ("En proceso", "En proceso"),
        ("Finalizado", "Finalizado"),
        ("Cancelado", "Cancelado"),
    ]

    titulo = models.CharField(max_length=40)
    descripcion = models.TextField(max_length=500)
    presupuesto = models.DecimalField(max_digits=20, decimal_places=2)
    estado = models.TextField(max_length=20, choices=state_choices)
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, null=True)
    responsable = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = "PROYECTO"
