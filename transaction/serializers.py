from rest_framework import serializers
from transaction.models import Transaction
from banks.models import Banks
from django.contrib.auth import get_user_model

Client = get_user_model()


class TransactionSerializer(serializers.ModelSerializer):
    receiver = serializers.CharField(max_length=10, required=True)
    transaction_type = serializers.CharField(max_length=10, required=True)

    class Meta:
        model = Transaction
        fields = ["bank", "amount", "receiver", "transaction_type"]

    def validate(self, attrs):
        receiver_acc_no = Client.objects.filter(account_number=attrs["receiver"])
        bank = Banks.objects.filter(id=attrs["bank"].id)

        if receiver_acc_no.exists() and bank.exists():
            return attrs

        else:
            raise serializers.ValidationError(
                {"error-message": f"Pls receheck the account or bank provided."}
            )

    def create(self, validated_data):
        if validated_data["transaction_type"] == "deposit":
            sender = Client.objects.get(id=self.context["request"].user.id)
            receiver = Client.objects.get(account_number=validated_data["receiver"])

            if (
                sender.account_number == validated_data["receiver"]
            ):  # This checks if the money is deposited to sender account number
                sender.account_balance += validated_data["amount"]
                print("****", sender.account_balance)
            else:
                receiver.account_balance += validated_data[
                    "amount"
                ]  # This checks if the money is deposited into another account number
                receiver.save()
            Transaction.objects.create(
                amount=validated_data["amount"],
                sender=self.context["request"].user,
                receiver=validated_data["receiver"],
                bank=validated_data["bank"],
                transaction_type=validated_data["transaction_type"],
            )
            return validated_data

        elif validated_data["transaction_type"] == "withdraw":
            sender = Client.objects.get(id=self.context["request"].user.id)

            if sender.account_balance < validated_data["amount"]:
                raise serializers.ValidationError(
                    {"info": "Your have less then the money you want to withdraw"}
                )
            else:
                sender.account_balance -= validated_data["amount"]
                sender.save()
                validated_data[
                    "amount_left"
                ] = f"You have {sender.account_balance} left"
                Transaction.objects.create(
                    amount=validated_data["amount"],
                    sender=self.context["request"].user,
                    receiver=validated_data["receiver"],
                    bank=validated_data["bank"],
                    transaction_type=validated_data["transaction_type"],
                )
                return validated_data


class TransactionDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["amount", "bank", "receiver", "transaction_type", "date"]
