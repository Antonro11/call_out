from rest_framework.permissions import BasePermission


class AuthenticatedNotAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and not request.user.is_superuser:
            return True
        return False


class AuthenticatedAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        return False
