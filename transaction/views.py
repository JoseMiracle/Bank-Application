from rest_framework import generics, permissions
from transaction.serializers import TransactionSerializer, TransactionDetailsSerializer
from transaction.models import Transaction


class TransactionAPIView(generics.CreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class TransactionDetailsAPIView(generics.ListAPIView):
    serializer_class = TransactionDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get"]

    def get_queryset(self):
        return Transaction.objects.all().filter(sender=self.request.user)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
