from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Estado, Cidade

class EstadoSerializer(serializers.ModelSerializer):
    total_cidades = serializers.SerializerMethodField()
    
    class Meta:
        model = Estado
        fields = ['id', 'nome', 'sigla', 'regiao', 'total_cidades', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
    
    def get_total_cidades(self, obj):
        return obj.cidades.count()

class CidadeSerializer(serializers.ModelSerializer):
    estado_nome = serializers.CharField(source='estado.nome', read_only=True)
    estado_sigla = serializers.CharField(source='estado.sigla', read_only=True)
    usuario_nome = serializers.CharField(source='usuario.username', read_only=True)
    
    class Meta:
        model = Cidade
        fields = [
            'id', 'nome', 'estado', 'estado_nome', 'estado_sigla',
            'populacao', 'area_km2', 'pib', 'foto', 'usuario', 'usuario_nome',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at', 'usuario']
    
    def create(self, validated_data):
        validated_data['usuario'] = self.context['request'].user
        return super().create(validated_data)

class CidadeUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = ['foto']

class CidadeDetailSerializer(serializers.ModelSerializer):
    estado = EstadoSerializer(read_only=True)
    usuario_nome = serializers.CharField(source='usuario.username', read_only=True)
    
    class Meta:
        model = Cidade
        fields = [
            'id', 'nome', 'estado', 'populacao', 'area_km2', 'pib', 'foto',
            'usuario', 'usuario_nome', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at', 'usuario']