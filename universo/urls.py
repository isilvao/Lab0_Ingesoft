from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_person/", views.addPerson, name="addPerson"),
    path("gestion_personas/", views.gestion_personas, name="gestion_personas"),
    path(
        "gestion_personas/eliminarPersona/<int:id>",
        views.eliminar_persona,
        name="eliminar_persona",
    ),
]
