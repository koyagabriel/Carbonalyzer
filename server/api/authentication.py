from rest_framework_simplejwt.authentication import JWTAuthentication as JWTAuth
from rest_framework_simplejwt.exceptions import AuthenticationFailed


def default_user_authentication_rule(user):
    return user is not None and \
           user.is_active and \
           not user.deleted


class JWTAuthentication(JWTAuth):

    def get_user(self, validated_token):
        user = super().get_user(validated_token)

        if user.deleted:
            raise AuthenticationFailed('User not found', code='user_not_found')

        return user
