from rest_framework import generics, permissions, status
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from rest_framework.response import Response

from accounts.serializers import (
    SignUpSerializer,
    SignInSerializer,
    ChangePasswordSerializer,
    UpdateProfileSerializer,
    AccountBalanceSerializer,
)

Client = get_user_model()


class SignUpAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class SignInAPIView(TokenObtainPairView):
    serializer_class = SignInSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ChangePasswordAPIView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChangePasswordSerializer
    http_method_names = ["patch"]
    queryset = Client.objects.all()

    def get_object(self):
        return self.request.user

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


class UpdateProfileAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdateProfileSerializer
    queryset = Client.objects.all()
    http_method_names = ["put"]

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)


class AccountBalanceAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AccountBalanceSerializer
    http_method_names = ["get"]

    def get_object(self):
        return self.request.user


class DeleteAccountAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["delete"]
    lookup_field = "pk"

    def get_queryset(self):
        return Client.objects.all()

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
