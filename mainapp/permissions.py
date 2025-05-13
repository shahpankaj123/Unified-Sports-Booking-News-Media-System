from rest_framework.permissions import BasePermission
from .models import Users

class AdminUserPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return bool(False)
        if request.user is None:
            return bool(False)
        user_type = Users.objects.get(email=request.user)
        if user_type == 'Admin':
            return bool(True)
        return bool(False)
    
class VenueUserPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return bool(False)
        if request.user is None:
            return bool(False)
        user_type = Users.objects.get(email=request.user)
        if user_type == 'VenueUsers':
            return bool(True)
        return bool(False) 

class NormalUserPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return bool(False)
        if request.user is None:
            return bool(False)
        user_type = Users.objects.get(email=request.user)
        if user_type == 'NormalUsers':
            return bool(True)
        return bool(False)        