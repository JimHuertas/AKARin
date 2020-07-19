from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Import models
from .models import Documento

def home(request):
    documentos = Documento.objects.all()
    return render(request, "myapp/home.html", {"documentos": documentos ,"titulo": "Bienvenido"})

#Para la busqueda
def busqueda(request):
    return render(request, 'myapp/busqueda.html', {"titulo": "Busqueda"})

#View que procesará el pedido de busqueda
def buscar(request):
    if request.GET["search"]:
        doc = request.GET["search"]

        documentos = Documento.objects.filter(nombre__icontains=doc)
        return render(request, 'myapp/busqueda.html',{"elemento": doc, "documentos":documentos, "warning" : True, "titulo": "Busqueda"} )

    else:
        return render(request, 'myapp/busqueda.html',{"elemento": doc, "documentos":documentos, "titulo": "Busqueda"} )


def cargar(request):
    if request.method == "POST":
        name = request.POST["nombre"]
        typ = request.POST["tipo"]
        etiqueta = request.POST["tag"]
        fil = request.POST["file"]

        Documento.objects.create(nombre=name, tipo=typ, tag=etiqueta, doc=fil)
        return render(request, 'myapp/cargar.html', {"titulo": "Subir"})

    return render(request, 'myapp/cargar.html', {"titulo": "Subir"})

#view para cargar al servidor
def loading(request):
    pass


def help(request):
    return render(request, 'myapp/help.html', {"titulo": "Ayuda"})