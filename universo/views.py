from django.shortcuts import render

def index(request):
    return render(request, "gestionPersonas.html")

def add_person(request):
    # lógica para la vista add_person
    return render(request, 'add_person.html')

def gestion_personas(request):
    # lógica para la vista gestion_personas
    personas = [...]  # Obtén la lista de personas desde tu base de datos o modelo
    return render(request, 'gestionPersonas.html', {'personas': personas})