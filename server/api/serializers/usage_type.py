from rest_framework.serializers import ModelSerializer
from api.models.usage_type import UsageType


class UsageTypeSerializer(ModelSerializer):

    class Meta:
        model = UsageType
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
