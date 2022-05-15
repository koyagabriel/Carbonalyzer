from rest_framework.serializers import ModelSerializer
from api.models.usage import Usage


class UsageSerializer(ModelSerializer):

    class Meta:
        model = Usage
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
