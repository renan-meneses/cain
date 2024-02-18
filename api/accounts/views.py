from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User  # noqa: F401, E261
from .serializers import MyTokenObtainPairSerializer, RegistrationSerializer


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
            data["response"] = "Registration Successful!"
            refresh = RefreshToken.for_user(user=user)
            data["refresh"] = str(refresh)
            data["access"] = str(refresh.access_token)

        return Response(data, status.HTTP_201_CREATED)


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
