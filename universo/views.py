from django.shortcuts import render

def index(request):
    return render(request, "home.html")

def add_person(request):
    # lógica para la vista add_person
    return render(request, 'add_person.html')

def gestion_personas(request):
<<<<<<< Updated upstream
    # lógica para la vista gestion_personas
    personas = [...]  # Obtén la lista de personas desde tu base de datos o modelo
    return render(request, 'gestionPersonas.html', {'personas': personas})
=======

    personas = Persona.objects.all()

    for persona in personas:
        print(persona.cabeza_de_familia)

    return render(request, "gestionPersonas.html", {"personas": personas})

def gestion_viviendas(request):

    # personas = Persona.objects.all()

    # for persona in personas:
    #     print(persona.cabeza_de_familia)

    return render(request, "gestionViviendas.html")

def gestion_municipios(request):

    # personas = Persona.objects.all()

    # for persona in personas:
    #     print(persona.cabeza_de_familia)

    return render(request, "gestionMunicipios.html")
>>>>>>> Stashed changes
