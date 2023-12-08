from rest_framework import permissions as perms

class IsAdminOrSelf(perms.IsAdminUser):
    """
    Allow access to admin users or the user himself.
    """
    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_staff:
            return True
        elif (request.user and type(obj) == type(request.user) and
              obj == request.user):
            return True
        return False