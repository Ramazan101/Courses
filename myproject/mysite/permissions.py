from rest_framework.permissions import BasePermission

class StudentPermissions(BasePermission):
     def has_permission(self, request, view):
        return request.user.role == 'student'


class TeacherPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'teacher'