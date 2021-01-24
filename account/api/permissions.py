from rest_framework.permissions import AllowAny, IsAdminUser, BasePermission, SAFE_METHODS

class IsCustomerOrReadOnly(BasePermission):
    message = 'You must be the owner of this Customer profile'

    def has_object_permission(self, request, view, obj):
        if request in SAFE_METHODS:
            return True
        return obj.user == request.user