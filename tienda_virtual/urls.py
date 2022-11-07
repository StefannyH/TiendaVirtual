"""tienda_virtual URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventario.views import busqueda_producto, obtener_producto, mostrar_productos, agregar_producto, editar_producto, eliminar_producto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('busqueda_producto/', busqueda_producto),
    path('obtener_producto/', obtener_producto),
    path('mostrar_productos/', mostrar_productos, name = 'show-prods'),
    path('agregar_producto/', agregar_producto, name ='add-prods'),
    path('editar_producto/<int:parametro>', editar_producto),
    path('eliminar_producto/<int:parametro>', eliminar_producto),
]
