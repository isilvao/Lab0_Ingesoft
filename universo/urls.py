from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Página principal
    path("contacto/", views.contacto, name="contacto"),  # Página de contacto
    path("agregarPersona/", views.agregarPersona, name="agregarPersona"),
    path("", views.index, name="index"),
    path("add_person/", views.add_person, name="add_person"),
    path("gestion_personas/", views.gestion_personas, name="gestion_personas"),
]
