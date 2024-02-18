from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True
    )  # noaq: E501

    class Meta:
        model = User
        fields = ["email", "user_name", "password", "password2"]
        extra_kwargs = {"password": {"write_only": True}}

    """
    Save method to create a new user and store in the database.
    Returns: User: The newly created user object.
    """

    def save(self):
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password != password2:
            raise serializers.ValidationError(
                {"error": "passwords did not match"}
            )  # noaq: E501

        user = User(
            email=self.validated_data["email"],
            user_name=self.validated_data["user_name"],
            is_active=True,
        )
        user.set_password(self.validated_data["password"])
        user.save()
        return user


class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()
