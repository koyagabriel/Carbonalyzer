from rest_framework_simplejwt.views import TokenObtainPairView
from api.serializers.token import TokenSerializer


class TokenView(TokenObtainPairView):
    serializer_class = TokenSerializer
