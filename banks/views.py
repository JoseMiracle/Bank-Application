from rest_framework import generics, permissions
from banks.serializers import CreateBankSerializer


class CreateBankAPIView(generics.CreateAPIView):
    serializer_class = CreateBankSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
