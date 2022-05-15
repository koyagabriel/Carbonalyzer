from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from api.serializers.user import UserSerializer


class TokenSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        user_data = UserSerializer(self.user).data
        data.update(user_data)
        return data
