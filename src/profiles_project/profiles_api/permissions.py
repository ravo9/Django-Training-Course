from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile."""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile."""

        # We wanna allow user to see all profiles, but not to change them.

        # Is it a GET method?
        if request.method in permissions.SAFE_METHODS:
            return True

        # If it's not GET - does the user try to modify his own profile?
        return obj.id == request.user.id
