from django.db import models


class Persona(models.Model):
    choices_sexo = [
        ("M", "Masculino"),
        ("F", "Femenino"),
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
        "Vivienda", on_delete=models.CASCADE, null=True, blank=True
    )
    cabeza_de_familia = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "PERSONA"


class Municipio(models.Model):
    nombre = models.CharField(max_length=45)
    area = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    presupuesto = models.TextField(null=True, blank=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "MUNICIPIO"


class Vivienda(models.Model):
    direccion = models.CharField(max_length=45)
    capacidad = models.BigIntegerField()
    niveles = models.BigIntegerField(null=True, blank=True)
    area = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    propietario = models.ForeignKey(
        Persona,
        on_delete=models.CASCADE,
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
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    class Meta:
        db_table = "MUNICIPIO_has_EVENTO"


class PersonaEvento(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    class Meta:
        db_table = "PERSONA_goes_EVENTO"


class Proyecto(models.Model):
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=40)
    descripcion = models.TextField(max_length=500)
    presupuesto = models.BigIntegerField()
    estado = models.CharField(max_length=50)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = "PROYECTO"
