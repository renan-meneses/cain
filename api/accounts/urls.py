from django.urls import path  # isort:skip
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    DemoView,
    DemoView2,
    LogoutBlacklistTokenUpdateView,
    MyTokenObtainPairView,
    RegistrationAPIView,
    VerifyOTPAPIView,
)

urlpatterns = [
    path("login/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("verify/", VerifyOTPAPIView.as_view(), name="verify-otp"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", LogoutBlacklistTokenUpdateView.as_view(), name="logout"),
    path("register/", RegistrationAPIView.as_view(), name="registration"),
    path("experiment/", DemoView.as_view(), name="demo"),
    path("experiment2/", DemoView2.as_view(), name="demo2"),
]
