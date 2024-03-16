

from rest_framework import permissions
from rest_framework.permissions import BasePermission
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Allow all read-only requests
        if request.method in permissions.SAFE_METHODS:
            return True

        # Only allow authenticated users to perform non-read-only requests
        return request.user.is_authenticated and request.user.is_staff