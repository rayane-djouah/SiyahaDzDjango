from rest_framework.permissions import BasePermission

class IsCentralEmployee(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return hasattr(user, 'centralemployee')

class IsRegionalEmployee(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return hasattr(user, 'regionalemployee')

    def has_object_permission(self, request, view, obj):
        #obj is a city
        user = request.user
        if hasattr(user, 'regionalemployee'):
            return user.regionalemployee.region == obj.region
        return False

class IsTourist(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return hasattr(user, 'tourist')
    
    def has_object_permission(self, request, view, obj):
        #obj is a comment
        user = request.user
        if hasattr(user, 'tourist'):
            return user == obj.tourist.user
        return False