from django.urls import path  # isort:skip
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    LogoutBlacklistTokenUpdateView,
    MyTokenObtainPairView,
    RegistrationAPIView,
)

urlpatterns = [
    path("login/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", LogoutBlacklistTokenUpdateView.as_view(), name="logout"),
    path("register/", RegistrationAPIView.as_view(), name="registration"),
]
