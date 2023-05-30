from rest_framework import permissions

class IsManagerOrTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.type == "Student":
            return False
        else:
            return True
        
class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.type == "Manager":
            return True
        else:
            return False
        