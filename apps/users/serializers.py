from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from apps.news.models import News
from apps.news.serializers import NewsSerializer
from apps.users.models import Profile, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "phone_number", "email")


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    author_set = NewsSerializer(many=True)

    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "image",
            "info",
            "role",
            "post_view_count",
            "telegram",
            "instagram",
            "facebook",
            "twitter",
            "author_set",
        )


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            "image",
            "info",
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

    def create(self, validated_data):
        try:
            user = User.objects.create_user(**validated_data)
        except Exception as e:
            raise ValidationError(str(e))
        return user
