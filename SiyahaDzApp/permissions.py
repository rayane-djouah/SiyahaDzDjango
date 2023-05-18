from rest_framework import permissions


class IsCentralEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.centralemployee is not None
