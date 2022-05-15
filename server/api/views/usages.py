from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from api.serializers.usage import UsageSerializer
from api.models.usage import Usage
from api.permissions import IsUsageCreator


class UsageListCreateView(ListCreateAPIView):
    serializer_class = UsageSerializer
    queryset = Usage.objects.not_deleted()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data | {"user": request.user.id}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        return self.request.user.usages.all()


class UsageRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = UsageSerializer
    queryset = Usage.objects.not_deleted()
    permission_classes = [IsAuthenticated, IsUsageCreator]
    lookup_url_kwarg = "id"
