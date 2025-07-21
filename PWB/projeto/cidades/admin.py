from django.contrib import admin
from .models import Estado, Cidade

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sigla', 'regiao', 'total_cidades', 'created_at']
    list_filter = ['regiao', 'created_at']
    search_fields = ['nome', 'sigla']
    ordering = ['nome']
    
    def total_cidades(self, obj):
        return obj.cidades.count()
    total_cidades.short_description = 'Total de Cidades'

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'estado', 'populacao', 'usuario', 'created_at']
    list_filter = ['estado', 'estado__regiao', 'created_at', 'usuario']
    search_fields = ['nome', 'estado__nome', 'estado__sigla']
    raw_id_fields = ['usuario']
    ordering = ['nome']
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('estado', 'usuario')
