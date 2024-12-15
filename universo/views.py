from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    municipio_nombre = "Pamplonita"
    return render(
        request, "universo/index.html", {"municipio_nombre": municipio_nombre}
    )


def contacto(request):
    if request.method == "POST":
        # Lógica para procesar el formulario
        nombre = request.POST["name"]
        email = request.POST["email"]
        mensaje = request.POST["message"]

        # Procesar los datos (ejemplo: guardarlos en la base de datos o enviarlos por correo)
        # Aquí solo estamos mostrando una respuesta de ejemplo.
        return HttpResponse(
            f"Gracias por tu mensaje, {nombre}. Nos pondremos en contacto contigo pronto."
        )

    return render(request, "universo/contacto.html")
