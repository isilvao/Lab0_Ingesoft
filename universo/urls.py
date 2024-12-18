from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_person/", views.agregar_persona, name="agregar_persona"),
    path("gestion_personas/", views.gestion_personas, name="gestion_personas"),
    path(
        "gestion_personas/eliminarPersona/<int:id>",
        views.eliminar_persona,
        name="eliminar_persona",
    ),
    path("agregar_vivienda/", views.agregar_vivienda, name="agregar_vivienda"),
    path("agregar_municipio/", views.agregar_municipio, name="agregar_municipio"),
]
