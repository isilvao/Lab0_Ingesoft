from django.shortcuts import render
from django.http import HttpResponse
from universo.models import Persona


def index(request):
    return render(request, "gestionPersonas.html")


def add_person(request):
    # lógica para la vista add_person
    return render(request, "add_person.html")


def contacto(request):
    if request.method == "POST":
        # Lógica para procesar el formulario
        nombre = request.POST["name"]
        email = request.POST["email"]
        mensaje = request.POST["message"]

        # Procesar los datos (ejemplo: guardarlos en la base de datos o enviarlos por correo)
        # Aquí solo estamos mostrando una respuesta de ejemplo.
        return HttpResponse(
            f"Gracias por tu mensaje, {nombre}. Nos pondremos en contacto contigo pronto."
        )

    return render(request, "universo/contacto.html")


def agregarPersona(request):
    if request.method == "POST":
        # Lógica para procesar el formulario
        nombre = request.POST["nombre"]
        telefono = request.POST["telefono"] if "telefono" in request.POST else None
        edad = request.POST["edad"]
        sexo = request.POST["sexo"]
        ahorros = request.POST["ahorros"] if "ahorros" in request.POST else 0.0
        vivienda_residencial = (
            request.POST["vivienda_residencial"]
            if "vivienda_residencial" in request.POST
            else None
        )
        cabeza_de_familia = (
            request.POST["cabeza_de_familia"]
            if "cabeza_de_familia" in request.POST
            else None
        )

        try:
            edad = int(edad)
        except ValueError:
            return HttpResponse("La edad debe ser un número")

        try:
            ahorros = float(ahorros)
        except ValueError:
            return HttpResponse("Los ahorros deben ser un número decimal")

        if telefono:
            try:
                telefono = int(telefono)
            except ValueError:
                return HttpResponse("El teléfono debe ser un número")

        # Validaciones
        if not nombre:
            return HttpResponse("El nombre es requerido")
        if not edad:
            return HttpResponse("La edad es requerida")
        if not sexo:
            return HttpResponse("El sexo es requerido")

        if edad < 0 or edad > 150:
            return HttpResponse("La edad debe ser un número entre 0 y 150")
        if sexo not in ["M", "F", "O", "N"]:
            return HttpResponse(
                "El sexo debe ser Masculino, Femenino, Otro o Prefiero no reponder"
            )
        if ahorros and ahorros < 0:
            return HttpResponse("Los ahorros deben ser un número positivo")

        # Procesar los datos
        persona = Persona(
            nombre=nombre,
            telefono=telefono,
            edad=edad,
            sexo=sexo,
            ahorros=ahorros,
            vivienda_residencial=vivienda_residencial,
            cabeza_de_familia=cabeza_de_familia,
        )

        try:
            persona.save()
        except Exception as e:
            return HttpResponse(f"Error: {e}")
        #
        return HttpResponse(
            f"Gracias por tu mensaje, {nombre}. Nos pondremos en contacto contigo pronto."
        )

    return render(request, "universo/index.html")


def gestion_personas(request):
    # lógica para la vista gestion_personas
    personas = [...]  # Obtén la lista de personas desde tu base de datos o modelo
    return render(request, "gestionPersonas.html", {"personas": personas})
