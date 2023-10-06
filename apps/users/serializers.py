from django.core import signing
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import gettext_lazy as _

from apps.users.cache import CacheTypes
from apps.users.models import User, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "phone_number", "email")


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "surname",
            "image",
            "info",
            "role",
            "telegram",
            "instagram",
            "facebook",
            "twitter",
        )


class RegisterUserSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField()
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("id", "first_name", "phone_number", "password", "token")

    def get_token(self, user):
        tokens = RefreshToken.for_user(user)
        data = {"refresh": str(tokens), "access": str(tokens.access_token)}
        return data

    # def validate(self, attrs):
    #     phone_data = attrs.pop("phone_number")
    #     signer = signing.TimestampSigner()
    #     phone_data = signer.unsign_object(phone_data, max_age=600)
    #     if phone_data.get("type") != CacheTypes.registration_sms_verification:
    #         raise ValidationError(_("Wrong type!"))
    #     attrs["phone_number"] = phone_data.get("phone")
    #     return attrs

    def create(self, validated_data):
        try:
            user = User.objects.create_user(**validated_data)
        except Exception as e:
            raise ValidationError(str(e))
        return user


class RecoveryCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField()

    def validate(self, attrs):
        phone_number = attrs.get("phone_number")
        if not User.objects.filter(phone_number=phone_number).exists():
            raise ValidationError("This user does not exists. ")
        return attrs


class SendCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "phone_number"]

    def validate_phone_number(self, phone_number):
        if User.objects.filter(phone_number=phone_number).exists():
            raise ValidationError(
                f"A user with the phone number {phone_number} already exists."
            )
        return phone_number


class VerificationRegistrationCodeSerializer(SendCodeSerializer):
    code = serializers.CharField()
    session = serializers.CharField()

    class Meta(SendCodeSerializer.Meta):
        fields = SendCodeSerializer.Meta.fields + ["code", "session"]


class RecoveryCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField()

    def validate(self, attrs):
        phone_number = attrs.get("phone_number")
        if not User.objects.filter(phone_number=phone_number).exists():
            raise ValidationError("This user does not exists. ")
        return attrs


class VerificationRecoverySerializer(RecoveryCodeSerializer):
    code = serializers.CharField()
    session = serializers.CharField()


class RecoverySetPasswordSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        phone_data = attrs.pop("phone_number")
        signer = signing.TimestampSigner()
        phone_data = signer.unsign_object(phone_data, max_age=600)
        print(phone_data)
        if phone_data.get("type") != CacheTypes.forget_pass_verification:
            raise ValidationError(_("Wrong type!"))
        attrs["phone_number"] = phone_data.get("phone")
        return attrs

    def create(self, validated_data):
        try:
            phone = validated_data.get("phone_number")
            password = validated_data.get("password")
            user = User.objects.get(phone_number=phone)
            user.set_password(password)
            user.save()
        except Exception as e:
            raise ValidationError(str(e))
        return user
