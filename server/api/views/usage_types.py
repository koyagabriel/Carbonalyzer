from rest_framework.generics import (ListAPIView, RetrieveUpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from api.serializers.usage_type import UsageTypeSerializer
from api.models.usage_type import UsageType


class UsageTypesListView(ListAPIView):
    serializer_class = UsageTypeSerializer
    queryset = UsageType.objects.not_deleted()
    permission_classes = [IsAuthenticated]


class UsageTypeRetrieveView(RetrieveUpdateAPIView):
    serializer_class = UsageTypeSerializer
    queryset = UsageType.objects.not_deleted()
    lookup_url_kwarg = "id"
    permission_classes = [IsAuthenticated]
