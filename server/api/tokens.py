from rest_framework_simplejwt.tokens import (
    AccessToken as AccessToken_,
    BlacklistMixin,
    RefreshToken as RefreshToken_
)


class AccessToken(BlacklistMixin, AccessToken_):
    """
    subclassing the AccessToken class with a blacklist mixin.
    This adds the ability to blacklist access type tokens which
    wasn't implemented by default
    """
    token_type = "access"


class RefreshToken(RefreshToken_):
    """
    Subclassing the Refresh token in order make use of the
    custom AccessToken when creating an access token.
    """
    access_token_class = AccessToken
