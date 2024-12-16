from django.shortcuts import render, redirect
from django.http import HttpResponse
from universo.models import Persona, Vivienda


def index(request):
    return render(request, "gestionPersonas.html")


def eliminar_persona(request, id):
    persona = Persona.objects.get(id=id)
    persona.delete()
    return redirect("/gestion_personas/")


def addPerson(request):
    if request.method == "POST":
        # Lógica para procesar el formulario
        nombre = request.POST["nombre"]
        telefono = request.POST["telefono"]
        edad = request.POST["edad"]
        sexo = request.POST["sexo"]
        ahorros = request.POST["ahorros"]
        vivienda_residencial = (
            int(request.POST["vivienda_residencial"])
            if "vivienda_residencial" in request.POST
            else None
        )
        cabeza_de_familia = int(request.POST["cabeza_de_familia"])

        if ahorros == "":
            ahorros = 0.0
        if telefono == "":
            telefono = None
        if vivienda_residencial == "":
            vivienda_residencial = None
        else:
            if not Vivienda.objects.filter(pk=vivienda_residencial).exists():
                vivienda_residencial = None
            else:
                vivienda_residencial = Vivienda.objects.get(pk=vivienda_residencial)
        if cabeza_de_familia == "":
            cabeza_de_familia = None

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
            cabeza_de_familia=Persona.objects.get(pk=cabeza_de_familia),
        )

        try:
            persona.save()
        except Exception as e:
            return HttpResponse(f"Error: {e}")
        #
        return render(request, "addPerson.html", {"success": True})

    personas = Persona.objects.all()
    viviendas = Vivienda.objects.all()

    return render(
        request,
        "addPerson.html",
        {"success": False, "personas": personas, "viviendas": viviendas},
    )


def gestion_personas(request):

    personas = Persona.objects.all()

    for persona in personas:
        print(persona.cabeza_de_familia)

    return render(request, "gestionPersonas.html", {"personas": personas})
