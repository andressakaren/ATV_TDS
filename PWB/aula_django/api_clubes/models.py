from django.db import models
from django.utils import timezone

# Create your models here.

class Clube(models.Model):
    nome_time = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.nome_time

class Jogador(models.Model):
    nome_jogador = models.CharField(max_length=50)
    clube = models.ForeignKey(
        Clube,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    def __str__(self) -> str:
        return self.nome_jogador
    