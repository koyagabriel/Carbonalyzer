from django.urls import path
from api.views.token import (TokenView, TokenRefreshView, TokenBlacklistView)
from api.views.users import (UsersCreateView, UserProfileView, UserProfileUpdateView)
from api.views.usage_types import (UsageTypesListView, UsageTypeRetrieveView)
from api.views.usages import (UsageListCreateView, UsageRetrieveUpdateView)

urlpatterns = [
    path("register", UsersCreateView.as_view(), name="registration"),
    path("token", TokenView.as_view(), name="token"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout", TokenBlacklistView.as_view(), name="logout"),
    path("profile", UserProfileView.as_view(), name="user_profile"),
    path("profile/update", UserProfileUpdateView.as_view(), name="user_profile_update"),
    path("usage-types", UsageTypesListView.as_view(), name="usage_types"),
    path("usage-types/<int:id>", UsageTypeRetrieveView.as_view(), name="retrieve_usage_types"),
    path("usages", UsageListCreateView.as_view(), name="usages"),
    path("usages/<int:id>", UsageRetrieveUpdateView.as_view(), name="retrieve_update_usages")
]
