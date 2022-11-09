from django.contrib import admin
from inventario.models import Productos
from import_export.admin import ExportActionMixin

# Register your models here.
class ProductosAdmin(ExportActionMixin, admin.ModelAdmin):

    list_display = ('name', 'cost')
    search_fields = ('name', )
    list_filter  = ('category', 'cantidad_stock')
    


admin.site.register(Productos,ProductosAdmin)
