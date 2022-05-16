from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenBlacklistSerializer as TokenBlacklistSerializer_
)
from api.tokens import RefreshToken, AccessToken
from api.serializers.user import UserSerializer


class TokenSerializer(TokenObtainPairSerializer):
    token_class = RefreshToken

    def validate(self, attrs):
        data = super().validate(attrs)
        user_data = UserSerializer(self.user).data
        data.update(user_data)
        return data


class TokenBlacklistSerializer(TokenBlacklistSerializer_):
    token_class = RefreshToken
    access_token_class = AccessToken
    access = serializers.CharField()

    def validate(self, attrs):
        refresh = self.token_class(attrs["refresh"])
        access = self.access_token_class(attrs["access"])
        try:
            refresh.blacklist()
            access.blacklist()
        except AttributeError:
            pass
        return {}
