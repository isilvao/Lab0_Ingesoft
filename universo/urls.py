from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("gestion_personas/", views.gestion_personas, name="gestion_personas"),
    path("add_person/", views.agregar_persona, name="agregar_persona"),
    path(
        "gestion_personas/eliminarPersona/<int:id>",
        views.eliminar_persona,
        name="eliminar_persona",
    ),
    path("gestion_personas/edit_person/<int:persona_id>/", views.editar_persona, name="editar_persona"),

    path("gestion_viviendas/", views.gestion_viviendas, name="gestion_viviendas"),
    path("agregar_vivienda/", views.agregar_vivienda, name="agregar_vivienda"),
    path("gestion_viviendas/edicionVivienda/<int:vivienda_id>/", views.editar_vivienda, name="editar_vivienda"),

    path(
        "gestion_viviendas/eliminarVivienda/<int:id>",
        views.eliminar_vivienda,
        name="eliminar_vivienda",
    ),
    path("gestion_municipios/", views.gestion_municipios, name="gestion_municipios"),
    path("agregar_municipio/", views.agregar_municipio, name="agregar_municipio"),
    path("gestion_municipios/edicionMunicipio/<int:municipio_id>/", views.editar_municipio, name="editar_municipio"),
    path(
        "gestion_municipios/eliminarMunicipio/<int:id>",
        views.eliminar_municipio,
        name="eliminar_municipio",
    ),
    path("gestion_proyectos/", views.gestion_proyectos, name="gestion_proyectos"),
    path("agregar_proyecto/", views.agregar_proyecto, name="agregar_proyecto"),
    path(
        "gestion_proyectos/eliminarProyecto/<int:id>",
        views.eliminar_proyecto,
        name="eliminar_proyecto",
    ),
    path("gestion_eventos/", views.gestion_eventos, name="gestion_eventos"),
    path("agregar_evento/", views.agregar_evento, name="agregar_evento"),
    path(
        "gestion_eventos/eliminarEvento/<int:id>",
        views.eliminar_evento,
        name="eliminar_evento",
    ),
]
