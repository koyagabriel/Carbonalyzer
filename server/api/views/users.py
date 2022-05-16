from rest_framework.generics import (CreateAPIView, RetrieveAPIView, UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from api.serializers.user import (UserSerializer, UpdateUserProfileSerializer)
from api.models.user import User


class UsersCreateView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.not_deleted()


class UserProfileView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.not_deleted()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserProfileUpdateView(UpdateAPIView):
    serializer_class = UpdateUserProfileSerializer
    queryset = User.not_deleted()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
