from django.urls import path

from .views import ListEnterprise

urlpatterns = [
    path("enterprise/", ListEnterprise.as_view(), name="enterprise"),
]
