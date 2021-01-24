from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly, SAFE_METHODS

class MyIsAdminOrReadOnly(BasePermission):
    message = 'You need to be a manager (staff or admin)'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff or request.user.is_superuser