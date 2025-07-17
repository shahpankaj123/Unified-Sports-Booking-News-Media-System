from rest_framework import permissions

from .permissions import AdminUserPermission,VenueUserPermission,NormalUserPermission
from rest_framework.authentication import TokenAuthentication

class AdminUserPermissionMixin:
    permission_classes = [permissions.IsAuthenticated, AdminUserPermission]
    authentication_classes = [TokenAuthentication]

class VenueUserPermissionMixin:
    permission_classes = [permissions.IsAuthenticated, VenueUserPermission] 
    authentication_classes = [TokenAuthentication]   

class NormalUserPermissionMixin:
    permission_classes = [permissions.IsAuthenticated, NormalUserPermission] 
    authentication_classes = [TokenAuthentication]   