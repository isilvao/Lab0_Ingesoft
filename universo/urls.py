from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Página principal
    path("contacto/", views.contacto, name="contacto"),  # Página de contacto
    path("agregarPersona/", views.agregarPersona, name="agregarPersona"),
]
