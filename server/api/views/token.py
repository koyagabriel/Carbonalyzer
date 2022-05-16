from django.conf import settings
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView as TokenRefreshView_,
    TokenBlacklistView as TokenBlacklistView_
)
from rest_framework_simplejwt.exceptions import (InvalidToken, TokenError)
from rest_framework import status
from rest_framework.response import Response
from api.serializers.token import (TokenSerializer, TokenBlacklistSerializer)


class TokenMixin:

    def process(self, serializer):
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        validated_data = serializer.validated_data
        refresh_token = validated_data.pop('refresh')
        response = Response(serializer.validated_data, status=status.HTTP_200_OK)
        response.set_cookie('jwt', value=refresh_token, httponly=True, max_age=24 * 60 * 60)
        return response


class TokenView(TokenMixin, TokenObtainPairView):
    serializer_class = TokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        return self.process(serializer)


class TokenRefreshView(TokenMixin, TokenRefreshView_):

    def post(self, request, *args, **kwargs):
        token = request.COOKIES.get('jwt', None)
        serializer = self.get_serializer(data={"refresh": token})
        return self.process(serializer)


class TokenBlacklistView(TokenBlacklistView_):
    serializer_class = TokenBlacklistSerializer
    
    def get_header(self, request):
        
        if hasattr(settings, 'AUTH_HEADER_NAME'):
            return request.META.get(settings.AUTH_HEADER_NAME)
        
        return request.META.get(api_settings.AUTH_HEADER_NAME)

    def get_auth_header_types(self):
        if hasattr(settings, 'AUTH_HEADER_TYPES'):
            auth_header_types = settings.AUTH_HEADER_TYPES
        else:
            auth_header_types = api_settings.AUTH_HEADER_TYPES

        if not isinstance(auth_header_types, (list, tuple)):
            auth_header_types = (auth_header_types,)

        return auth_header_types

    def get_raw_access_token(self, request):
        header = self.get_header(request)
        auth_header_types = self.get_auth_header_types()
        parts = header.split()

        if len(parts) == 0:
            return None

        if parts[0] not in auth_header_types:
            return None

        if len(parts) != 2:
            return None

        return parts[1]

    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get('jwt', None)
        access_token = self.get_raw_access_token(request)
        serializer = self.get_serializer(data={"refresh": refresh_token, "access": access_token})
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError:
            pass

        response = Response({}, status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie('jwt')
        return response



