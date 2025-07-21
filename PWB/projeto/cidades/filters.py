import django_filters
from .models import Estado, Cidade

class EstadoFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')
    sigla = django_filters.CharFilter(lookup_expr='iexact')
    regiao = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Estado
        fields = ['nome', 'sigla', 'regiao']

class CidadeFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')
    estado__nome = django_filters.CharFilter(lookup_expr='icontains')
    estado__sigla = django_filters.CharFilter(lookup_expr='iexact')
    estado__regiao = django_filters.CharFilter(lookup_expr='icontains')
    populacao_min = django_filters.NumberFilter(field_name='populacao', lookup_expr='gte')
    populacao_max = django_filters.NumberFilter(field_name='populacao', lookup_expr='lte')
    area_min = django_filters.NumberFilter(field_name='area_km2', lookup_expr='gte')
    area_max = django_filters.NumberFilter(field_name='area_km2', lookup_expr='lte')
    
    class Meta:
        model = Cidade
        fields = [
            'nome', 'estado', 'estado__nome', 'estado__sigla', 'estado__regiao',
            'populacao_min', 'populacao_max', 'area_min', 'area_max'
        ]
