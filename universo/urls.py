from django.urls import path
from . import views

urlpatterns = [
<<<<<<< Updated upstream
    path('', views.index, name='index'),
    path('add_person/', views.add_person, name='add_person'),
    path('gestion_personas/', views.gestion_personas, name='gestion_personas'),
    
=======
    path("", views.index, name="index"),
    path("add_person/", views.addPerson, name="addPerson"),
    path("gestion_personas/", views.gestion_personas, name="gestion_personas"),
    path(
        "gestion_personas/eliminarPersona/<int:id>",
        views.eliminar_persona,
        name="eliminar_persona",
    ),
    path("gestion_viviendas/", views.gestion_viviendas, name="gestion_viviendas"),
    path("gestion_municipios/", views.gestion_municipios, name="gestion_municipios"),
>>>>>>> Stashed changes
]
 