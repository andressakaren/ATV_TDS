from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Estado, Cidade
from .serializers import (
    EstadoSerializer, CidadeSerializer, CidadeDetailSerializer, CidadeUploadSerializer
)
from .permissions import IsOwnerOrReadOnly, IsOwner
from .filters import EstadoFilter, CidadeFilter
from .mixins import OwnerFilterMixin

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    filterset_class = EstadoFilter
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['nome', 'sigla', 'regiao']
    ordering_fields = ['nome', 'sigla', 'created_at']
    ordering = ['nome']
    
    @swagger_auto_schema(
        method='get',
        operation_description="Lista todas as cidades de um estado",
        responses={200: CidadeSerializer(many=True)}
    )
    @action(detail=True, methods=['get'])
    def cidades(self, request, pk=None):
        estado = self.get_object()
        cidades = estado.cidades.all()
        serializer = CidadeSerializer(cidades, many=True, context={'request': request})
        return Response(serializer.data)

class CidadeViewSet(OwnerFilterMixin, viewsets.ModelViewSet):
    queryset = Cidade.objects.select_related('estado', 'usuario')
    serializer_class = CidadeSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filterset_class = CidadeFilter
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['nome', 'estado__nome', 'estado__sigla']
    ordering_fields = ['nome', 'populacao', 'area_km2', 'created_at']
    ordering = ['nome']
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CidadeDetailSerializer
        elif self.action == 'upload_foto':
            return CidadeUploadSerializer
        return CidadeSerializer
    
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
    
    @swagger_auto_schema(
        method='put',
        operation_description="Upload de foto para uma cidade",
        manual_parameters=[
            openapi.Parameter(
                'foto',
                openapi.IN_FORM,
                description="Arquivo de imagem",
                type=openapi.TYPE_FILE,
                required=True
            )
        ],
        responses={200: CidadeUploadSerializer()}
    )
    @action(
        detail=True, 
        methods=['put'], 
        permission_classes=[IsAuthenticated, IsOwner],
        parser_classes=[MultiPartParser, FormParser]
    )
    def upload_foto(self, request, pk=None):
        cidade = self.get_object()
        serializer = CidadeUploadSerializer(cidade, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)