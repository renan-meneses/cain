from rest_framework import generics, permissions, serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .email import *  # noqa: F403, F401
from .models import User
from .serializers import (
    MyTokenObtainPairSerializer,
    RegistrationSerializer,
    VerifyOTPSerializer,
)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    throttle_scope = "login"


class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        print(request)
        serializer = self.get_serializer(data=request.data)
        data = {}
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            # send_otp(serializer.data["email"])  # noqa: F405
            data["response"] = "Registration Successful!"
            refresh = RefreshToken.for_user(user=user)
            data["refresh"] = str(refresh)
            data["access"] = str(refresh.access_token)

        return Response(data, status.HTTP_201_CREATED)


class VerifyOTPSerializer(serializers.Serializer):  # noqa: F811
    email = serializers.EmailField()
    otp = serializers.CharField()


class VerifyOTPAPIView(generics.GenericAPIView):
    serializer_class = VerifyOTPSerializer

    def post(self, request, *args, **kwargs):
        serializer = VerifyOTPSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data["email"]
            otp = serializer.data["otp"]
            user_obj = User.objects.get(email=email)

            if user_obj.otp == otp:
                user_obj.is_staff = True
                user_obj.save()
                return Response("verified")
            return Response(serializer.data, status.HTTP_400_BAD_REQUEST)


class LogoutBlacklistTokenUpdateView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:  # noqa: F841
            return Response(status=status.HTTP_400_BAD_REQUEST)


class DemoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            return Response("accessed")
        except Exception as e:
            print(e)
            return Response("")


class DemoView2(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            return Response("accessed 2")
        except Exception as e:
            print(e)
            return Response("")
