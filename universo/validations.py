from universo.models import Persona, Vivienda, Municipio


def validatePersona(request):
    nombre = request.POST["nombre"]
    telefono = request.POST["telefono"]
    edad = request.POST["edad"]
    sexo = request.POST["sexo"]
    ahorros = request.POST["ahorros"]
    vivienda = (
        int(request.POST["vivienda_residencial"])
        if "vivienda_residencial" in request.POST
        else None
    )
    cabezaFamilia = (
        int(request.POST["cabeza_de_familia"])
        if "cabeza_de_familia" in request.POST
        else None
    )

    if ahorros == "":
        ahorros = 0.0
    if telefono == "":
        telefono = None
    if vivienda == "":
        vivienda = None
    else:
        if not Vivienda.objects.filter(pk=vivienda).exists():
            vivienda = None
        else:
            vivienda = Vivienda.objects.get(pk=vivienda)
    if cabezaFamilia == "":
        cabezaFamilia = None
    else:
        if not Persona.objects.filter(pk=cabezaFamilia).exists():
            cabezaFamilia = None
        else:
            cabezaFamilia = Persona.objects.get(pk=cabezaFamilia)

    try:
        edad = int(edad)
    except ValueError:
        return False, "La edad debe ser un número"

    try:
        ahorros = float(ahorros)
    except ValueError:
        return False, "Los ahorros deben ser un número decimal"

    if telefono:
        try:
            telefono = int(telefono)
        except ValueError:
            return False, "El teléfono debe ser un número"

    # Validaciones
    if nombre == "":
        return False, "El nombre es requerido"
    if edad == "":
        return False, "La edad es requerida"
    if sexo == "":
        return False, "El sexo es requerido"

    if edad < 0 or edad > 150:
        return False, "La edad debe ser un número entre 0 y 150"
    if sexo not in ["H", "M", "O", "N"]:
        return False, "El sexo debe ser Hombre, Mujer, Otro o Prefiero no reponder"

    if ahorros and ahorros < 0:
        return False, "Los ahorros deben ser un número positivo"

    # Procesar los datos
    persona = Persona(
        nombre=nombre,
        telefono=telefono,
        edad=edad,
        sexo=sexo,
        ahorros=ahorros,
        vivienda_residencial=vivienda,
        cabeza_de_familia=cabezaFamilia,
    )

    return True, persona


def validateVivienda(request):
    direccion = request.POST["direccion"]
    capacidad = request.POST["capacidad"]
    niveles = request.POST["niveles"]
    area = request.POST["area"]
    municipio = request.POST["municipio"] if "municipio" in request.POST else None
    propietario = request.POST["propietario"] if "propietario" in request.POST else None

    if capacidad == "" or not capacidad.isdigit() or int(capacidad) < 0:
        return False, "La capacidad es obligatoria debe ser un número entero positivo"
    else:
        capacidad = int(capacidad)

    if niveles == "" or not niveles.isdigit() or int(niveles) < 0:
        return (
            False,
            "Los niveles son obligatorios y deben ser un número entero positivo",
        )
    else:
        niveles = int(niveles)

    if area == "":
        return False, "El área es obligatoria y debe ser un número positivo"
    else:
        try:
            float(area)
            if float(area) < 0:
                return False, "El área debe ser un número positivo"
        except ValueError:
            return False, "El área debe ser un número decimal"

    if direccion == "":
        return False, "La dirección es obligatoria"

    if municipio == "" or not Municipio.objects.filter(pk=municipio).exists():
        return False, "Escoja un municipio válido"
    else:
        municipio = Municipio.objects.get(pk=municipio)

    if propietario == "" or not Persona.objects.filter(pk=propietario).exists():
        return False, "Escoja un propietario válido"
    else:
        propietario = Persona.objects.get(pk=propietario)

    vivienda = Vivienda(
        direccion=direccion,
        capacidad=capacidad,
        niveles=niveles,
        area=area,
        municipio=municipio,
        propietario=propietario,
    )

    return True, vivienda


def validateMunicipio(request):
    nombre = request.POST["nombre"]
    area = request.POST["area"]
    presupuesto = request.POST["presupuesto"]
    persona = request.POST["persona"] if "persona" in request.POST else None

    if area == "":
        return False, "El área es obligatoria y debe ser un número positivo"
    else:
        try:
            float(area)
            if float(area) < 0:
                return False, "El área debe ser un número positivo"
        except ValueError:
            return False, "El área debe ser un número decimal"

    if nombre == "":
        return False, "El nombre es obligatorio"
    else:
        if Municipio.objects.filter(nombre=nombre).exists():
            return False, "Ya existe un municipio con ese nombre"

    if presupuesto == "" or not presupuesto.isdigit() or float(presupuesto) < 0:
        return False, "El presupuesto es obligatorio y debe ser un número positivo"
    else:
        presupuesto = float(presupuesto)

    if persona == "" or not Persona.objects.filter(pk=persona).exists():
        return False, "Escoja una persona válida"
    else:
        persona = Persona.objects.get(pk=persona)

    municipio = Municipio(
        nombre=nombre, area=area, presupuesto=presupuesto, persona=persona
    )

    return True, municipio
