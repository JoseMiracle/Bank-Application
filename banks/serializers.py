from rest_framework import serializers
from banks.models import Banks


class CreateBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banks
        fields = ["bank_name"]

    def validate(self, attrs):
        errors = {}
        bank_name = Banks.objects.filter(bank_name=attrs["bank_name"])

        if bank_name.exists():
            errors["Info"] = f"Warning: The Bank *{attrs['bank_name']}* exists"
            raise serializers.ValidationError(errors)
        else:
            return attrs

    def create(self, validated_data):
        return super().create(validated_data)

    def to_representation(self, instance):
        return super().to_representation(instance)
