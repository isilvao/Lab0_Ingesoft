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
    validateMunicipioParaEditar
)
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

def index(request):
    return render(request, "home.html")


# PERSONAS
def eliminar_persona(request, id):
    persona = Persona.objects.get(id=id)
    persona.delete()
    messages.success(request, 'Persona eliminada exitosamente.')
    return redirect("/gestion_personas/")


def agregar_persona(request):
    if request.method == "POST":

        # Validaciones
        resultado, respuesta = validatePersona(request)

        personas = Persona.objects.all()
        viviendas = Vivienda.objects.all()


        if resultado:
            try:
                respuesta.save()
                messages.success(request, 'Persona agregada exitosamente.')
            except Exception as e:
                return render(
                    request,
                    "addPerson.html",
                    {
                        "success": False,
                        "error": e,
                        "personas": personas, "viviendas": viviendas
                    },
                    status=400,
                )
            #
            return redirect("/add_person/")
        else:
            return render(
                request,
                "addPerson.html",
                {
                    "success": False,
                    "error": respuesta,
                    "personas": personas, "viviendas": viviendas
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
    viviendas = Vivienda.objects.all()
    return render(request, "gestionPersonas.html", {"personas": personas, "viviendas": viviendas})

@csrf_exempt
def editar_persona(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)  # Busca la persona o devuelve 404

    personas = Persona.objects.all()
    viviendas = Vivienda.objects.all()

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
                # return render(
                #     request,
                #     "edicionPersona.html",
                #     {"success": False, "error": str(e)},
                #     status=400,
                # )
                return render(
                    request,
                    #cambiar esto
                    "edicionPersona.html",
                    {"success": False, "error": str(e)},
                    status=400,
                )
            messages.success(request, 'Información editada exitosamente.')
            return redirect("/gestion_personas/")

        else:
            # return render(
            #     request,
            #     "edicionPersona.html",
            #     {"success": False, "error": respuesta},
            #     status=400,
            # )
            return render(
                    request,
                    #cambiar esto
                    "edicionPersona.html",
                    {
                        "success": False,
                        "error": respuesta,
                        
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
                    status=400
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
        personas = Persona.objects.all()
        municipios = Municipio.objects.all()

        resultado, respuesta = validateVivienda(request)

        if resultado:
            try:
                respuesta.save()
                messages.success(request, 'Vivienda agregada correctamente.')
            except Exception as e:
                # return render(
                #     request,
                #     "agregarVivienda.html",
                #     {
                #         "success": False,
                #         "error": respuesta,
                #     },
                #     status=400,
                    
                # )
                return render(
                        request,
                        "agregarVivienda.html",
                        {"success": None, "personas": personas, "municipios": municipios,"error": respuesta,},status=400,
                    )
                # return HttpResponse("Error: " + str(e))
            return render(request, "agregarVivienda.html", {"success": True, "personas": personas, "municipios": municipios})
            # return HttpResponse("Vivienda agregada correctamente")
        else:
            return render(
                request,
                "agregarVivienda.html",
                {
                    "success": False,
                    "error": respuesta,
                },
                status=400,
            )

            # return HttpResponse("Error: " + str(respuesta), status=400)

    personas = Persona.objects.all()
    municipios = Municipio.objects.all()

    
    return render(
        request,
        "agregarVivienda.html",
        {"success": None, "personas": personas, "municipios": municipios},
    )
   
    # return HttpResponse("Viviendas: " + str(personas) + str(municipios))

@csrf_exempt
def editar_vivienda(request, vivienda_id):
    vivienda = get_object_or_404(Vivienda, id=vivienda_id)  # Busca la vivienda o devuelve 404
    personas = Persona.objects.all()
    municipios = Municipio.objects.all()

    if request.method == "POST":
        # Validaciones
        resultado, respuesta = validateVivienda(request)

        if resultado:
            try:
                # Actualizar campos existentes con los datos validados
                vivienda.direccion = respuesta.direccion
                vivienda.capacidad = respuesta.capacidad
                vivienda.niveles = respuesta.niveles
                vivienda.area = respuesta.area
                vivienda.municipio = respuesta.municipio
                vivienda.propietario = respuesta.propietario
                vivienda.save()
            except Exception as e:
                return render(
                    request,
                    "edicionVivienda.html",
                    {
                        "success": False,
                        "error": str(e),
                        "vivienda": {
                            "id": vivienda.id,
                            "direccion": vivienda.direccion,
                            "capacidad": vivienda.capacidad,
                            "niveles": vivienda.niveles,
                            "area": vivienda.area,
                            "municipio": vivienda.municipio.id if vivienda.municipio else None,
                            "propietario": vivienda.propietario.id if vivienda.propietario else None,
                        },
                        "personas": personas,
                        "municipios": municipios,
                    },
                    status=400,
                )
            messages.success(request, "Información editada exitosamente.")
            return redirect("/gestion_viviendas/")

        else:
            return render(
                request,
                "edicionVivienda.html",
                {
                    "success": False,
                    "error": respuesta,
                    "vivienda": {
                        "id": vivienda.id,
                        "direccion": vivienda.direccion,
                        "capacidad": vivienda.capacidad,
                        "niveles": vivienda.niveles,
                        "area": vivienda.area,
                        "municipio": vivienda.municipio.id if vivienda.municipio else None,
                        "propietario": vivienda.propietario.id if vivienda.propietario else None,
                    },
                    "personas": personas,
                    "municipios": municipios,
                },
                status=400,
            )

    # En caso de GET, se envían los datos actuales de la vivienda
    return render(
        request,
        "edicionVivienda.html",
        {
            "success": None,
            "vivienda": {
                "id": vivienda.id,
                "direccion": vivienda.direccion,
                "capacidad": vivienda.capacidad,
                "niveles": vivienda.niveles,
                "area": vivienda.area,
                "municipio": vivienda.municipio.id if vivienda.municipio else None,
                "propietario": vivienda.propietario.id if vivienda.propietario else None,
            },
            "personas": personas,
            "municipios": municipios,
        },
    )


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
        personas = Persona.objects.all()


        resultado, respuesta = validateMunicipio(request)

        if resultado:
            try:
                respuesta.save()
                messages.success(request, 'Municipio agregado correctamente.')
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
                # return HttpResponse("Error: " + str(e))
            # return render(request, "agregarMunicipio.html", {"success": True})
            return render(
                request,
                "agregarMunicipio.html",
                {"success": True, "personas": personas},
            )
            # return HttpResponse("Municipio agregado correctamente")
        else:
            
            return render(
                request,
                "agregarMunicipio.html",
                {
                    "success": False,
                    "error": respuesta,
                },
                status=400,
            )
            
            # return HttpResponse("Error: " + str(respuesta), status=400)

    personas = Persona.objects.all()

    
    return render(
        request,
        "agregarMunicipio.html",
        {"success": None, "personas": personas},
    )
    
    # return HttpResponse("Municipios: " + str(personas))

@csrf_exempt
def editar_municipio(request, municipio_id):
    municipio = get_object_or_404(Municipio, id=municipio_id)  # Busca el municipio o devuelve 404
    personas = Persona.objects.all()  # Obtiene todas las personas (para el campo `persona`)

    if request.method == "POST":
        # Validaciones
        resultado, respuesta = validateMunicipioParaEditar(request, municipio_id)

        if resultado:
            try:
                # Actualizar campos existentes con los datos validados
                municipio.nombre = respuesta.nombre
                municipio.area = respuesta.area
                municipio.presupuesto = respuesta.presupuesto
                municipio.persona = respuesta.persona
                municipio.save()
                messages.success(request, "Información editada exitosamente.")
            except Exception as e:
                return render(
                    request,
                    "edicionMunicipio.html",
                    {
                        "success": False,
                        "error": str(e),
                        "municipio": {
                            "id": municipio.id,
                            "nombre": municipio.nombre,
                            "area": municipio.area,
                            "presupuesto": municipio.presupuesto,
                            "persona": municipio.persona.id if municipio.persona else None,
                        },
                        "personas": personas,
                    },
                    status=400,
                )
            
            return redirect("/gestion_municipios/")

        else:


            return render(
                request,
                "edicionMunicipio.html",
                {
                    "success": False,
                    "error": respuesta,
                    "municipio": {
                        "id": municipio.id,
                        "nombre": municipio.nombre,
                        "area": municipio.area,
                        "presupuesto": municipio.presupuesto,
                        "persona": municipio.persona.id if municipio.persona else None,
                    },
                    "personas": personas,
                },
                status=400,
            )

    # En caso de GET, se envían los datos actuales del municipio
    return render(
        request,
        "edicionMunicipio.html",
        {
            "success": None,
            "municipio": {
                "id": municipio.id,
                "nombre": municipio.nombre,
                "area": municipio.area,
                "presupuesto": municipio.presupuesto,
                "persona": municipio.persona.id if municipio.persona else None,
            },
            "personas": personas,
        },
    )

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
                return render(
                    request,
                    "agregarProyecto.html",
                    {
                        "success": False,
                        "error": respuesta,
                    },
                    status=400,
                )
                #return HttpResponse("Error: " + str(e))
            return render(request, "agregarProyecto.html", {"success": True})
            # return HttpResponse("Proyecto agregado correctamente")
        else:
            return render(
                request,
                "agregarProyecto.html",
                {
                    "success": False,
                    "error": respuesta,
                },
                status=400,
            )
            #return HttpResponse("Error: " + str(respuesta), status=400)

    personas = Persona.objects.all()
    municipios = Municipio.objects.all()

    return render(
        request,
        "agregarProyecto.html",
        {"success": None, "personas": personas, "municipios": municipios},
    )

    #return HttpResponse("Proyectos: " + str(personas) + str(municipios))

@csrf_exempt
def editar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)  # Busca el proyecto o devuelve 404
    municipios = Municipio.objects.all()  # Lista de municipios para selección
    personas = Persona.objects.all()  # Lista de responsables para selección

    if request.method == "POST":
        # Validar datos del formulario
        resultado, respuesta = validateProyecto(request)

        if resultado:
            try:
                # Actualizar campos existentes con los datos validados
                proyecto.titulo = respuesta.titulo
                proyecto.descripcion = respuesta.descripcion
                proyecto.presupuesto = respuesta.presupuesto
                proyecto.estado = respuesta.estado
                proyecto.municipio = respuesta.municipio
                proyecto.responsable = respuesta.responsable
                proyecto.save()
            except Exception as e:
                return render(
                    request,
                    "edicionProyecto.html",
                    {
                        "success": False,
                        "error": str(e),
                        "proyecto": {
                            "id": proyecto.id,
                            "titulo": proyecto.titulo,
                            "descripcion": proyecto.descripcion,
                            "presupuesto": proyecto.presupuesto,
                            "estado": proyecto.estado,
                            "municipio": proyecto.municipio.id if proyecto.municipio else None,
                            "responsable": proyecto.responsable.id if proyecto.responsable else None,
                        },
                        "municipios": municipios,
                        "personas": personas,
                    },
                    status=400,
                )
            messages.success(request, "Información del proyecto editada exitosamente.")
            return redirect("/gestion_proyectos/")

        else:
            return render(
                request,
                "edicionProyecto.html",
                {
                    "success": False,
                    "error": respuesta,
                    "proyecto": {
                        "id": proyecto.id,
                        "titulo": proyecto.titulo,
                        "descripcion": proyecto.descripcion,
                        "presupuesto": proyecto.presupuesto,
                        "estado": proyecto.estado,
                        "municipio": proyecto.municipio.id if proyecto.municipio else None,
                        "responsable": proyecto.responsable.id if proyecto.responsable else None,
                    },
                    "municipios": municipios,
                    "personas": personas,
                },
                status=400,
            )

    # En caso de GET, se envían los datos actuales del proyecto
    return render(
        request,
        "edicionProyecto.html",
        {
            "success": None,
            "proyecto": {
                "id": proyecto.id,
                "titulo": proyecto.titulo,
                "descripcion": proyecto.descripcion,
                "presupuesto": proyecto.presupuesto,
                "estado": proyecto.estado,
                "municipio": proyecto.municipio.id if proyecto.municipio else None,
                "responsable": proyecto.responsable.id if proyecto.responsable else None,
            },
            "municipios": municipios,
            "personas": personas,
        },
    )


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
                
                return render(
                    request,
                    "agregarEvento.html",
                    {
                        "success": False,
                        "error": respuesta,
                    },
                    status=400,
                )
                
                # return HttpResponse("Error: " + str(e))
            return render(request, "agregarEvento.html", {"success": True})
            # return HttpResponse("Evento agregado correctamente")
        else:
            return render(
                request,
                "agregarEvento.html",
                {
                    "success": False,
                    "error": respuesta,
                },
                status=400,
            )
            
            # return HttpResponse("Error: " + str(respuesta), status=400)

    municipios = Municipio.objects.all()

    
    return render(
        request,
        "agregarEvento.html",
        {"success": None, "municipios": municipios},
    )
    
    # return HttpResponse("Eventos: " + str(municipios))


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
