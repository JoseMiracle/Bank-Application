from django.urls import path
from banks.views import CreateBankAPIView

urlpatterns = [
    path("create-bank/", CreateBankAPIView.as_view(), name="create-bank"),
]
