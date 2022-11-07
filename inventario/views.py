from itertools import product
from wsgiref.util import request_uri
from django.shortcuts import render, redirect
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


def agregar_producto(request):
     if request.method == 'POST':
         nombre = request.POST["nombre"]
         categoria = request.POST["categoria"]
         costo = request.POST["costo"]
         stock = request.POST["stock"]
         descripcion = request.POST["descripcion"]
         data = Productos(name=nombre, category=categoria, cost=costo, cantidad_stock= stock, description=descripcion)
         data.save()

         return redirect('/mostrar_productos/')
     else:
        return render(request,"add_products.html")


def editar_producto(request, parametro):
    productos = Productos.objects.get(id=parametro)
    if request.method == 'POST':
         productos.name = request.POST["nombre"]
         productos.category = request.POST["categoria"]
         productos.cost = request.POST["costo"]
         productos.cantidad_stock = request.POST["stock"]
         productos.description = request.POST["descripcion"]         
         productos.save()

         return redirect("/mostrar_productos/")
    else:
        return render(request,"edit_products.html",{'productos': productos})


def eliminar_producto(request, parametro):
    productos = Productos.objects.get(id=parametro)
    if request.method == 'POST':               
         productos.delete()

         return redirect("/mostrar_productos/")
    else:
        return render(request,"delete_products.html",{'productos': productos})
