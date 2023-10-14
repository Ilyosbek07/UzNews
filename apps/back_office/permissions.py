from rest_framework import permissions

from apps.users.choices import Role
from apps.users.models import Profile


class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        profile = Profile.objects.get(user=request.user.id)
        if Role.moderator == profile.role:
            return True
        else:
            return False


class IsAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        profile = Profile.objects.get(user=request.user.id)
        if Role.author == profile.role:
            return True
        else:
            return False
