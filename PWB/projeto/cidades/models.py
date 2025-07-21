from django.db import models
from django.contrib.auth.models import User

class Estado(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    sigla = models.CharField(max_length=2, unique=True)
    regiao = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
    
    def __str__(self):
        return f"{self.nome} ({self.sigla})"

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name='cidades')
    populacao = models.IntegerField(null=True, blank=True)
    area_km2 = models.FloatField(null=True, blank=True)
    pib = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    foto = models.ImageField(upload_to='cidades/', null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cidades')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        unique_together = ['nome', 'estado']
    
    def __str__(self):
        return f"{self.nome} - {self.estado.sigla}"
