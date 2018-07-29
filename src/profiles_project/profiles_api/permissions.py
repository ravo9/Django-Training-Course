from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile."""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile."""

        # We wanna allow user to see all profiles, but not to change them.

        # Is it a GET method?
        # If any user wants just to see that object - that's ok.
        if request.method in permissions.SAFE_METHODS:
            return True

        # The object is a profile.
        # If it's not GET - does the user try to modify his own profile?
        return obj.id == request.user.id


class PostOwnStatus(permissions.BasePermission):
    """Allow users to update their own status."""

    def has_object_permission(self, request, view, obj):
        """Check if the user if trying to update his own status."""

        # Is it a GET method?
        # If any user wants just to see that object - that's ok.
        if request.method in permissions.SAFE_METHODS:
            return True

        # The object is a status.
        return obj.user_profile.id == request.user.id
