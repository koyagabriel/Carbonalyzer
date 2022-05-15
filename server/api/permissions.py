from rest_framework.permissions import BasePermission


class IsUsageCreator(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.user.id
