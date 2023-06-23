from django.urls import path
from transaction.views import TransactionAPIView, TransactionDetailsAPIView

urlpatterns = [
    path("all-transactions/", TransactionAPIView.as_view(), name="send-money"),
    path(
        "transaction-details/",
        TransactionDetailsAPIView.as_view(),
        name="transaction-details",
    ),
]
