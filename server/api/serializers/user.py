from rest_framework.serializers import ModelSerializer
from api.models.user import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "email", "password",
                  "first_name", "last_name", "date_joined"]
        read_only_fields = ["id", "date_joined"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        instance = self.Meta.model(**validated_data)
        instance.set_password(password)
        instance.save()
        return instance


class UpdateUserProfileSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name"]
        read_only_field = ["id"]
