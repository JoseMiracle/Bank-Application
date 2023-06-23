from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
from banks.models import Banks
from django.utils import timezone

Client = get_user_model()


class Transaction(models.Model):
    TRANSACTION_TYPE = (
        ("deposit", "deposit"),
        ("withdraw", "withdraw"),
    )
    amount = models.IntegerField()
    bank = models.ForeignKey(Banks, on_delete=models.CASCADE)
    sender = models.ForeignKey(Client, on_delete=models.CASCADE)
    receiver = models.CharField(max_length=10, null=False, blank=False)
    transaction_type = models.CharField(
        max_length=10, choices=TRANSACTION_TYPE, null=True, blank=True
    )
    date = models.TimeField(default=timezone.now)
