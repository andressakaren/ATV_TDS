from django.db import models

class OwnerFilterMixin:
    """
    Mixin para filtrar objetos pelo usuário proprietário.
    """
    
    def get_queryset(self):
        return super().get_queryset().filter(usuario=self.request.user)
