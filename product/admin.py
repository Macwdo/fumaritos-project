from django.contrib import admin
from product.models import Produto, DadosVenda
# Register your models here.

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    ...
    
@admin.register(DadosVenda)
class DadosVendaAdmin(admin.ModelAdmin):
    ...
