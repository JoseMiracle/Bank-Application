from django.urls import path
from accounts.views import (
    SignUpAPIView,
    SignInAPIView,
    ChangePasswordAPIView,
    UpdateProfileAPIView,
    DeleteAccountAPIView,
    AccountBalanceAPIView,
)

urlpatterns = [
    path("sign-up/", SignUpAPIView.as_view(), name="sign-up"),
    path("sign-in/", SignInAPIView.as_view(), name="sign-in"),
    path("change-password/", ChangePasswordAPIView.as_view(), name="change-password"),
    path("update-profile/", UpdateProfileAPIView.as_view(), name="update-profile"),
    path(
        "delete-account/<int:pk>", DeleteAccountAPIView.as_view(), name="delete-account"
    ),
    path("account-balance/", AccountBalanceAPIView.as_view(), name="account-balance"),
]
