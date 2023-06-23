from django.urls import path
from transaction.views import TransactionAPIView, TransactionDetailsAPIView

urlpatterns = [
    path("any-transaction/", TransactionAPIView.as_view(), name="all-transactions"),
    path(
        "all-transaction-details/",
        TransactionDetailsAPIView.as_view(),
        name="transaction-details",
    ),
]
