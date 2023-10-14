from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        #Only Authenticated can see the list view
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        #Read permissions are allowed to any request so we'll always
        #allow GET, HEAD, or options requests
        if request.method in permissions.SAFE_METHODS:
            return True


            #Write permissions are only allowed tot he author of a post
        return obj.author == request.user