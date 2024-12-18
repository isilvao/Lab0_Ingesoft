from django.shortcuts import render, redirect
from django.http import HttpResponse
from universo.models import Persona, Vivienda, Municipio
from universo.validations import validatePersona, validateVivienda, validateMunicipio


def index(request):
    return render(request, "home.html")


# PERSONAS
def eliminar_persona(request, id):
    persona = Persona.objects.get(id=id)
    persona.delete()
    return redirect("/gestion_personas/")


def agregar_persona(request):
    if request.method == "POST":

        # Validaciones
        resultado, respuesta = validatePersona(request)

        if resultado:
            try:
                respuesta.save()
            except Exception as e:
                return render(
                    request,
                    "addPerson.html",
                    {
                        "success": False,
                        "error": e,
                    },
                    status=400,
                )
            #
            return render(request, "addPerson.html", {"success": True})
        else:
            return render(
                request,
                "addPerson.html",
                {
                    "success": False,
                    "error": respuesta,
                },
                status=400,
            )

    personas = Persona.objects.all()
    viviendas = Vivienda.objects.all()

    return render(
        request,
        "addPerson.html",
        {"success": None, "personas": personas, "viviendas": viviendas},
    )


def gestion_personas(request):

    personas = Persona.objects.all()

    return render(request, "gestionPersonas.html", {"personas": personas})


def gestion_municipios(request):

    # personas = Persona.objects.all()

    # for persona in personas:
    #     print(persona.cabeza_de_familia)

    return render(request, "gestionMunicipios.html")


def gestion_viviendas(request):
    viviendas = Vivienda.objects.all()
    return render(request, "gestionViviendas.html", {"viviendas": viviendas})


# VIVIENDAS
def agregar_vivienda(request):
    if request.method == "POST":

        resultado, respuesta = validateVivienda(request)

        if resultado:
            try:
                respuesta.save()
            except Exception as e:
                """
                return render(
                    request,
                    "agregarVivienda.html",
                    {
                        "success": False,
                        "error": respuesta,
                    },
                    status=400,
                )
                """
                return HttpResponse("Error: " + str(e))
            # return render(request, "agregarVivienda.html", {"success": True})
            return HttpResponse("Vivienda agregada correctamente")
        else:
            """
            return render(
                request,
                "agregarVivienda.html",
                {
                    "success": False,
                    "error": respuesta,
                },
                status=400,
            )
            """
            return HttpResponse("Error: " + str(respuesta), status=400)

    personas = Persona.objects.all()
    municipios = Municipio.objects.all()

    """
    return render(
        request,
        "agregarVivienda.html",
        {"success": None, "personas": personas, "municipios": municipios},
    )
    """
    return HttpResponse("Viviendas: " + str(personas) + str(municipios))

# MUNICIPIOS
def agregar_municipio(request):
    if request.method == "POST":

        resultado, respuesta = validateMunicipio(request)

        if resultado:
            try:
                respuesta.save()
            except Exception as e:
                """
                return render(
                    request,
                    "agregarMunicipio.html",
                    {
                        "success": False,
                        "error": respuesta,
                    },
                    status=400,
                )
                """
                return HttpResponse("Error: " + str(e))
            # return render(request, "agregarMunicipio.html", {"success": True})
            return HttpResponse("Municipio agregado correctamente")
        else:
            """
            return render(
                request,
                "agregarMunicipio.html",
                {
                    "success": False,
                    "error": respuesta,
                },
                status=400,
            )
            """
            return HttpResponse("Error: " + str(respuesta), status=400)

    personas = Persona.objects.all()

    """
    return render(
        request,
        "agregarMunicipio.html",
        {"success": None, "personas": personas},
    )
    """
    return HttpResponse("Municipios: " + str(personas))
