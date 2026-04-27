from rest_framework import permissions


class IsRoleBasedAccess(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.user.role == 'admin':
            return True

        if request.user.role == 'hr':
            return request.method in permissions.SAFE_METHODS

        return obj.user == request.user