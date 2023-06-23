from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import check_password
from django.core.mail import EmailMultiAlternatives
from banks.models import Banks

Client = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True, required=True)
    email = serializers.EmailField(write_only=True, required=True)
    home_address = serializers.CharField(required=True, write_only=True)
    image = serializers.ImageField(write_only=True, required=False)
    first_name = serializers.CharField(write_only=True)
    other_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    gender = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(write_only=True)
    account_type = serializers.CharField(write_only=True)

    class Meta:
        model = Client
        fields = [
            "bank",
            "first_name",
            "other_name",
            "last_name",
            "password",
            "email",
            "image",
            "home_address",
            "phone_number",
            "password",
            "account_type",
            "gender",
        ]

    def validate(self, attrs):
        email = Client.objects.filter(email=attrs["email"])

        if email.exists():
            raise serializers.ValidationError(
                {"error-message": f"The email: {attrs['email']} exists"}
            )

        phone = Client.objects.filter(phone_number=attrs["phone_number"])
        if phone.exists():
            raise serializers.ValidationError(
                {"error-message": f"The phone number: {attrs['phone_number']} exists"}
            )

        return attrs

    def create(self, validated_data):
        user = Client.objects.create_user(**validated_data)
        acc_number = validated_data["phone_number"][1:11]
        user.account_number = acc_number
        user.save()
        return user

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["Your Account Number:"] = instance.account_number
        data[
            "info"
        ] = f"Thank You {instance.first_name} {instance.last_name} {instance.other_name} for creating an account with us."
        return data


class SignInSerializer(TokenObtainPairSerializer):
    ...


class ChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["password"]

        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate_password(self, given_password):
        user = self.context["request"].user

        if len(given_password) < 8:
            raise serializers.ValidationError("Password is too short")

        elif check_password(given_password, user.password):
            raise serializers.ValidationError(
                "password can't be same as previous password"
            )
        return given_password

    def update(self, instance, validated_data):
        instance.set_password(validated_data["password"])
        instance.save()
        return instance

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["info"] = "Password changed Succesfully"
        return data


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "first_name",
            "last_name",
            "image",
            "other_name",
            "home_address",
            "phone_number",
            "email",
        ]

        extra_kwargs = {
            "image": {
                "required": False,
            },
            "email": {"required": False},
        }

    def validate(self, attrs):
        email = Client.objects.filter(email=attrs["email"])
        if email.exists():
            raise serializers.ValidationError(
                {"error-message": f"The email: {attrs['email']} exists"}
            )

        phone = Client.objects.filter(phone_number=attrs["phone_number"])
        if phone.exists():
            raise serializers.ValidationError(
                {"error-message": f"The phone number: {attrs['phone_number']} exists"}
            )

        return attrs

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        updated_profile = {}
        data = super().to_representation(instance)
        updated_profile["UPDATED-PROFILE"] = data
        data[
            "info"
        ] = f"{instance.first_name} {instance.last_name} your profile has been updated successfully"
        return updated_profile


class AccountBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["account_balance"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        del data["account_balance"]
        data[
            "info"
        ] = f"Welcome {self.context['request'].user.get_full_name()}, your account balance is {instance.account_balance}"
        return data
