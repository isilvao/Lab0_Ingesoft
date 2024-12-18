from django.shortcuts import render, redirect
from django.http import HttpResponse
from universo.models import (
    Persona,
    Proyecto,
    Vivienda,
    Municipio,
    Evento,
    MunicipioEvento,
)
from universo.validations import (
    validatePersona,
    validateVivienda,
    validateMunicipio,
    validateProyecto,
    validateEvento,
)
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404

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

@csrf_exempt
def editar_persona(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)  # Busca la persona o devuelve 404

    if request.method == "POST":
        # Validaciones
        resultado, respuesta = validatePersona(request)

        if resultado:
            try:
                # Actualizar campos existentes con los datos validados
                persona.nombre = respuesta.nombre
                persona.telefono = respuesta.telefono
                persona.edad = respuesta.edad
                persona.sexo = respuesta.sexo
                persona.ahorros = respuesta.ahorros
                persona.vivienda_residencial = respuesta.vivienda_residencial
                persona.cabeza_de_familia = respuesta.cabeza_de_familia
                persona.save()
            except Exception as e:
                return render(
                    request,
                    "edicionPersona.html",
                    {"success": False, "error": str(e)},
                    status=400,
                )
            return render(request, "edicionPersona.html", {"success": True})

        else:
            return render(
                request,
                "edicionPersona.html",
                {"success": False, "error": respuesta},
                status=400,
            )
        
    personas = Persona.objects.all()
    viviendas = Vivienda.objects.all()

    # En caso de GET, se envÃ­an los datos actuales de la persona
    return render(
        request,
        #cambiar esto
        "edicionPersona.html",
        {
            "success": None,
            "persona": {
                "id": persona.id,
                "nombre": persona.nombre,
                "telefono": persona.telefono,
                "edad": persona.edad,
                "sexo": persona.sexo,
                "ahorros": persona.ahorros,
                "vivienda_residencial": persona.vivienda_residencial.id if persona.vivienda_residencial else None,
                "cabeza_de_familia": persona.cabeza_de_familia.id if persona.cabeza_de_familia else None,
            },
            "personas": personas, "viviendas": viviendas,
        },
    )


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


def gestion_viviendas(request):
    viviendas = Vivienda.objects.all()
    return render(request, "gestionViviendas.html", {"viviendas": viviendas})


def eliminar_vivienda(request, id):
    vivienda = Vivienda.objects.get(id=id)
    vivienda.delete()
    return redirect("/gestion_viviendas/")


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


def gestion_municipios(request):

    municipios = Municipio.objects.all()

    return render(request, "gestionMunicipios.html", {"municipios": municipios})


def eliminar_municipio(request, id):
    municipio = Municipio.objects.get(id=id)
    municipio.delete()
    return redirect("/gestion_municipios/")


# PROYECTO
def agregar_proyecto(request):
    if request.method == "POST":

        resultado, respuesta = validateProyecto(request)

        if resultado:
            try:
                respuesta.save()
            except Exception as e:
                """
                return render(
                    request,
                    "agregarProyecto.html",
                    {
                        "success": False,
                        "error": respuesta,
                    },
                    status=400,
                )
                """
                return HttpResponse("Error: " + str(e))
            # return render(request, "agregarProyecto.html", {"success": True})
            return HttpResponse("Proyecto agregado correctamente")
        else:
            """
            return render(
                request,
                "agregarProyecto.html",
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
        "agregarProyecto.html",
        {"success": None, "personas": personas, "municipios": municipios},
    )
    """
    return HttpResponse("Proyectos: " + str(personas) + str(municipios))


def gestion_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, "gestionProyectos.html", {"proyectos": proyectos})


def eliminar_proyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    proyecto.delete()
    return redirect("/gestion_proyectos/")


# EVENTOS
def agregar_evento(request):
    if request.method == "POST":

        resultado, respuesta = validateEvento(request)

        if resultado:
            try:
                respuesta[0].save()
                respuesta[1].save()
            except Exception as e:
                """
                return render(
                    request,
                    "agregarEvento.html",
                    {
                        "success": False,
                        "error": respuesta,
                    },
                    status=400,
                )
                """
                return HttpResponse("Error: " + str(e))
            # return render(request, "agregarEvento.html", {"success": True})
            return HttpResponse("Evento agregado correctamente")
        else:
            """
            return render(
                request,
                "agregarEvento.html",
                {
                    "success": False,
                    "error": respuesta,
                },
                status=400,
            )
            """
            return HttpResponse("Error: " + str(respuesta), status=400)

    municipios = Municipio.objects.all()

    """
    return render(
        request,
        "agregarEvento.html",
        {"success": None, "municipios": municipios},
    )
    """
    return HttpResponse("Eventos: " + str(municipios))


def gestion_eventos(request):
    eventos = Evento.objects.all()

    resultados = MunicipioEvento.objects.select_related("municipio", "evento")

    for resultado in resultados:
        print(
            f"Evento: {resultado.evento.nombre}, Municipio: {resultado.municipio.nombre}"
        )

    return render(request, "gestionEventos.html", {"eventos": eventos})


def eliminar_evento(request, id):
    evento = Evento.objects.get(id=id)
    eventoMunicipio = MunicipioEvento.objects.get(evento=evento)
    eventoMunicipio.delete()
    evento.delete()
    return redirect("/gestion_eventos/")
