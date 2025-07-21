from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permissão personalizada que permite apenas ao proprietário do objeto editá-lo.
    """
    
    def has_permission(self, request, view):
        # Permissões de leitura para qualquer request,
        # então sempre permitir GET, HEAD ou OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Permissões de escrita apenas para usuários autenticados
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        # Permissões de leitura para qualquer request,
        # então sempre permitir GET, HEAD ou OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Permissões de escrita apenas para o proprietário do objeto.
        return obj.usuario == request.user

class IsOwner(permissions.BasePermission):
    """
    Permissão que permite acesso apenas ao proprietário do objeto.
    """
    
    def has_object_permission(self, request, view, obj):
        return obj.usuario == request.user