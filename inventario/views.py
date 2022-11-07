from itertools import product
from wsgiref.util import request_uri
from django.shortcuts import render
from inventario.models import Productos
from django.http import HttpResponse
# Create your views here.

def busqueda_producto(request):
    
    return render(request,"search_products.html")

def obtener_producto(request):
    producto = request.GET["prd"]
    return HttpResponse("El articulo buscado: %r" %producto)

def mostrar_productos(request):
    productos  = Productos.objects.all()
    return render(request,'show_products.html',{'productos':productos})