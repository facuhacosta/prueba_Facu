from django.contrib import admin
from GestionPedidos.models import clientes, articulos, pedidos

# Register your models here.

admin.site.register(clientes)
admin.site.register(articulos)
admin.site.register(pedidos)